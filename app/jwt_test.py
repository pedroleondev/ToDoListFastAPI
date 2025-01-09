import jwt
from datetime import datetime, timezone
# Configuração

# Chave secreta para assinatura do token
secret = "p1x@fl0w@#$"
payload = {
    "user_id": 232,
    "username": "leon",
    "exp": datetime.now(timezone.utc).timestamp() + 3600
}

# Criar o token JWT
token = jwt.encode(payload, secret, algorithm="HS256")
print("Token JWT:", token)

# Decodificar o token JWT
decoded = jwt.decode(token, secret, algorithms=["HS256"])
print("Payload Decodificado:", decoded)
