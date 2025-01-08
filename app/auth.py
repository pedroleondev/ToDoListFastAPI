from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt

# Chave secreta para assinatura do token
TOKEN = "segredo"

# Instância do esquema de autenticação, para extrair o token JWT de cada requisição
security = HTTPBearer()

# Função para obter o usuário atual a partir do token JWT
def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        payload = jwt.decode(credentials.credentials, TOKEN, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado!")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token Invalido!")
