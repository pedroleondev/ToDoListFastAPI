from datetime import timedelta, datetime, timezone
from typing import Annotated
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status
from app.models import User, CreateUserRequest, Token
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm
from jose import JWTError, jwt
from app.dependencies import user_dependency, db_dependency, oauth2_bearer

# Configuração

# Criar a rotas para autenticação, o APIRouter é utilizado para modularizar as rotas e facilitar a reutilização
router = APIRouter(prefix="/auth", tags=["Autenticação"])

# Chave secreta para assinatura do token
SECRET_KEY = "p1x@fl0w@#$"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 20

# bcrypt para criptografar a senha do usuário
bcrypt = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Criação das rotas de autenticação

# Rota para criação de um novo usuário
@router.post("/", status_code=status.HTTP_201_CREATED, summary="Criar novo usuário", description="Endpoint para criar um novo usuário.")
def create_user(db: db_dependency,
                create_user_request: CreateUserRequest):
    try:
        # Verificar antes se o usuário já existe
        usuario_existente = db.query(User).filter(User.usuario == create_user_request.usuario).first()
        if usuario_existente:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Usuário já existe!"
            )
        
        # Criar modelo de usuário para armazenar os dados do usuário
        create_user_model = User(
            usuario=create_user_request.usuario,
            senha=create_user_request.senha,
            senha_criptografada=bcrypt.hash(create_user_request.senha)
        )

        # Adicionar o usuário ao banco de dados
        db.add(create_user_model)
        db.commit()
        db.refresh(create_user_model)

        # Retornar uma mensagem de sucesso com o ID do usuário
        return {
            "message": "Usuário criado com sucesso!",
            "usuario_id": create_user_model.id
        }
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                             detail=f"Erro ao criar usuário: {str(e)}"
        )
    
# Rota para acesso com o token
@router.post("/token", response_model=Token)
def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: db_dependency):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Não foi possível validar o usuário."
        )
    
    token = create_access_token(
        username=user.usuario,
        user_id=user.id,
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))

    return {'access_token': token,
            'token_type': 'bearer',
            "message": f"Bem-Vindo, {user.usuario}"
    }

def authenticate_user(
        username: str, password: str, db):
    user = db.query(User).filter(User.usuario == username).first()
    if not user:
        return False
    if not bcrypt.verify(password, user.senha_criptografada):
        return False
    return user

def create_access_token(
        username: str, user_id: int, expires_delta: timedelta):
    encode = {
        'sub': username,
        'id': user_id
    }
    expires = datetime.now(timezone.utc) + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

