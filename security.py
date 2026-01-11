import time
from typing import Annotated
from uuid import uuid4

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from schemas.autenticacao import SchemaJWT, SchemaToken

PASSWORD = "teste"
ALGORITHM = "HS256"

def criar_jwt_token(id: int) -> SchemaToken:

    token_acesso = {
        "iss": "autenticacao.projeto-dio.com",
        "sub": id,
        "aud": "api.projeto-dio.com",
        "exp": time.time(),
        "jti": str(uuid4)
    }

    token = jwt.encode(token_acesso, PASSWORD, algorithm=ALGORITHM)
    return {"token": token}

def decodificar_token(token: str) -> SchemaJWT:
    try:
        token = jwt.decode(token, PASSWORD, algorithm=ALGORITHM)
        return token
    except jwt.ExpiredSignatureError as e:
        return {"msg": "O Token informado é inválido!"}
    except jwt.InvalidTokenError as i:
        return {"msg": "O Token está expirado"}
    
bearer = HTTPBearer()

async def valida_token(token: Annotated[HTTPAuthorizationCredentials, Depends(bearer)]):
    token = decodificar_token(token.credentials)
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Inválido!")
    
    return token


def valida_cliente(cliente: Annotated[int, Depends(valida_token)]):
    if not cliente:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Sem autorização de acesso")
        
    return cliente
