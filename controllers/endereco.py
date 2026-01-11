from fastapi import APIRouter, Depends
from services.endereco import buscar_enderecos_service, buscar_endereco_service, atualizar_endereco_service
from schemas.endereco import SchemaEnderecoUpdate
from view.endereco import SchemaEnderecoOut
from db.session import session
from sqlalchemy.ext.asyncio import AsyncSession
from security import valida_cliente

router = APIRouter(prefix="/enderecos", dependencies=[Depends(valida_cliente)], tags=["endereco"])

@router.get("/", response_model=list[SchemaEnderecoOut])
async def buscar_enderecos(sessao: AsyncSession = Depends(session)):
    resultado = await buscar_enderecos_service(sessao)
    return resultado

@router.get("/{id}", response_model=list[SchemaEnderecoOut])
async def buscar_endereco(id = int, sessao: AsyncSession = Depends(session)):
    resultado = await buscar_endereco_service(sessao, id)
    return resultado

@router.patch("/{id}", response_model=list[SchemaEnderecoUpdate])
async def atualizar_endereco(schema_endereco: SchemaEnderecoUpdate, id = int, sessao: AsyncSession = Depends(session)):
    resultado = await atualizar_endereco_service(schema_endereco, sessao, id)
    return resultado