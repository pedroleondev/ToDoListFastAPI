from typing import Annotated
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer

# Configuração
SECRET_KEY = "p1x@fl0w@#$"
ALGORITHM = "HS256"
bcrypt = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2PasswordBearer é utilizado para autenticação via OAuth2
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="/auth/token")

# Função para decodificar o token
def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        user_id: int = payload.get('id')
        if username is None or user_id is None:
            raise HTTPException(status_code=401, detail='Não foi possível validar o usuário.')
        return {'username': username, 'id': user_id}
    except JWTError:
        raise HTTPException(status_code=401, detail='Não foi possível validar o usuário')

# Dependência para obter o usuário atual
user_dependency = Annotated[dict, Depends(get_current_user)]

# Dependência para obter a sessão do banco de dados
db_dependency = Annotated[Session, Depends(get_db)]
