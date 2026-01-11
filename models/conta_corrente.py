from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Numeric, ForeignKey
from db.setup import Base

class ContaCorrente(Base):
    __tablename__ = "conta_corrente"
    id = Column(Integer, primary_key=True, autoincrement=True)
    limite = Column(Numeric(10,2), default=0.0)
    limite_saque = Column(Integer, default=0)
    id_conta = Column(Integer, ForeignKey("conta.id"), nullable=False, unique=True)
    
    conta = relationship("Conta", back_populates="conta_corrente")
