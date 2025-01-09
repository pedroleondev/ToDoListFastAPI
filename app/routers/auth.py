from datetime import timedelta, datetime
from typing import Annotated
from fastapi import APIRouter, HTTPException, Depends
from app.database import get_db, SessionLocal
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette import status
from app.models import User, CreateUserRequest, Token
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt

# Configuração

# Criar a rotas para autenticação, o APIRouter é utilizado para modularizar as rotas e facilitar a reutilização
router = APIRouter(prefix="/auth", tags=["Autenticação"])

# Chave secreta para assinatura do token
SECRET_KEY = "p1x@fl0w@#$"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 20

# bcrypt para criptografar a senha do usuário
bcrypt = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2PasswordBearer é utilizado para autenticação via OAuth2
# tokenUrl é a rota para obter o token de acesso
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="/auth/token")


# Função db_dependency para obter a sessão do banco de dados
# Annotated é utilizado para adicionar metadados ao parâmetro da função (Depends)
db_dependency = Annotated[Session, Depends(get_db)]

# Criação das rotas de autenticação

# Rota para criação de um novo usuário
@router.post("/", status_code=status.HTTP_201_CREATED, summary="Criar novo usuário", description="Endpoint para criar um novo usuário.")
# create_user cria um novo usuário no banco de dados
def create_user(db: db_dependency,
                create_user_request: CreateUserRequest):
    try:
        # modelo de usuário para armazenar os dados do usuário
        create_user_model = User(
            # utilizando o usuário informado na requisição
            usuario=create_user_request.usuario,
            # criptografando a senha informada na requisição
            senha=create_user_request.senha,
            senha_criptografada=bcrypt.hash(create_user_request.senha)
        )

        db.add(create_user_model)
        db.commit()
        db.refresh(create_user_model)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
# Rota para acesso com o token
@router.post("/token", response_model=Token)
# login_fro_acess_token permite o inicio da autenticação
def login_for_acess_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
                          db: db_dependency):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Não foi possível validar o usuário.")
    token = create_access_token(user.username, user.id, timedelta(minutes=20))

    return {'access_token': token, 'token_type': 'bearer'}

def authenticate_user(username: str, password: str, db):
    # Comparando o usuario do request com o cadastrado no Banco de dados
    user = db.query(User).filter(User.usuario == username).first()
    if not user:
        return False
    if bcrypt.verify(password, user.senha_criptografada):
        return False
    return user