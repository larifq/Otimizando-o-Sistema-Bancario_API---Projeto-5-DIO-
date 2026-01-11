from schemas.login import SchemaLogin, SchemaLoginResponse
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends
from db.session import session
from security import criar_jwt_token
from sqlalchemy import select
from models.login import Login

router = APIRouter(prefix="/login", tags=["login"])

@router.post("/")
async def realizar_login(login: SchemaLoginResponse):
    return criar_jwt_token(login.id)

@router.get("/")
async def buscar_endereco(sessao: AsyncSession = Depends(session)):
    select_endereco = await sessao.execute(select(Login))
    resultado = select_endereco.scalars().all()
    return  resultado
    
