from fastapi import APIRouter, Depends, status
from db.session import session
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.conta_corrente import SchemaContaCorrente, SchemaContaCorrenteUpdate
from services.conta_corrente import criar_conta_corrente_service
from services.conta_corrente import buscar_contas_corrente_service
from services.conta_corrente import buscar_conta_corrente_service
from services.conta_corrente import atualizar_conta_corrente_service
from security import valida_cliente

router = APIRouter(prefix='/contas_corrente', dependencies=[Depends(valida_cliente)], tags=["conta corrente"])


@router.post('/')
async def criar_conta_corrente(conta_corrente: SchemaContaCorrente, sessao: AsyncSession = Depends(session)):
    resultado = await criar_conta_corrente_service(sessao, conta_corrente)
    return resultado

@router.get('/')
async def buscar_contas_corrente(sessao: AsyncSession = Depends(session)):
    resultado = await buscar_contas_corrente_service(sessao)
    return resultado

@router.get('/{id}')
async def buscar_conta_corrente(id = int, sessao: AsyncSession = Depends(session)):
    resultado = await buscar_conta_corrente_service(sessao, id)
    return resultado

@router.get('/{id}')
async def buscar_conta_corrente(id = int, sessao: AsyncSession = Depends(session)):
    resultado = await buscar_conta_corrente_service(sessao, id)
    return resultado

@router.patch("/{id}")
async def atualizar_conta_corrente(conta_corrente: SchemaContaCorrenteUpdate, id = int, sessao: AsyncSession = Depends(session)):
    resultado = await atualizar_conta_corrente_service(conta_corrente, sessao, id)
    return resultado