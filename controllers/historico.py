from fastapi import APIRouter, Depends
from db.session import session
from services.historico import registrar_deposito_service
from services.historico import registrar_saque_service
from services.historico import buscar_historicos_service
from services.historico import buscar_saques_service
from services.historico import buscar_depositos_service
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.historico import SchemaHistorico, SchemaTransacao
from view.historico import SchemaHistoricoOut, SchemaDepositoOut, SchemaSaqueOut
from security import valida_cliente


router = APIRouter(prefix="/contas", dependencies=[Depends(valida_cliente)], tags=["historico"])



@router.post("/{id_conta}/historicos/deposito", response_model=SchemaDepositoOut)
async def registrar_deposito(transacao: SchemaTransacao, id_conta: int, sessao: AsyncSession = Depends(session)):
    resultado = await registrar_deposito_service(sessao, transacao, id_conta)
    return resultado

@router.post("/{id_conta}/historicos/saque", response_model=SchemaSaqueOut)
async def registrar_saque(transacao: SchemaTransacao, id_conta: int, sessao: AsyncSession = Depends(session)):
    resultado = await registrar_saque_service(sessao, transacao, id_conta)
    return resultado

@router.get("/{id_conta}/historicos", response_model=list[SchemaHistoricoOut])
async def buscar_historico(id_conta: int, sessao: AsyncSession = Depends(session)):
    resultado = await buscar_historicos_service(sessao, id_conta)
    return resultado

@router.get("/{id_conta}/historicos/saques", response_model=list[SchemaSaqueOut], response_model_exclude_none=True)
async def buscar_saques(id_conta: int, sessao: AsyncSession = Depends(session)):
    resultado = await buscar_saques_service(sessao, id_conta)
    return resultado

@router.get("/{id_conta}/historicos/depositos", response_model=list[SchemaDepositoOut], response_model_exclude_none=True)
async def buscar_depositos(id_conta: int, sessao: AsyncSession = Depends(session)):
    resultado = await buscar_depositos_service(sessao, id_conta)
    return resultado