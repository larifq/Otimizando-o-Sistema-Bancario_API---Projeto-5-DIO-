from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, CheckConstraint, DateTime

from db.setup import Base

class Historico(Base):
    __tablename__ = "historico"
    id = Column(Integer, primary_key=True, autoincrement=True)
    valor = Column(Numeric(10,2), nullable=False)
    tipo_transacao = Column(String(8), nullable=False)
    tipo_conta = Column(String(15), nullable=False)
    data_transacao = Column(DateTime, nullable=False)
    id_conta = Column(Integer, ForeignKey("conta.id"), nullable=False)

    conta = relationship("Conta", back_populates="historico")

    __table_args__ = (
        CheckConstraint(
            "tipo_transacao IN ('Saque', 'Deposito')",
            name="ck_tipo_transferencia"
        ),
        CheckConstraint(
            "tipo_conta IN ('Conta Corrente', 'Conta Poupança')",
            name="ck_tipo_conta")
    )
