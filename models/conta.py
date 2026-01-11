from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, ForeignKey, Numeric, String

from db.setup import Base


class Conta(Base):
    __tablename__ = "conta"
    id = Column(Integer, primary_key=True, autoincrement=True)
    saldo = Column(Numeric(10,2))
    agencia = Column(String(10), nullable=False)
    id_cliente = Column(Integer, ForeignKey("cliente.id"), nullable=False)
    
    

    cliente = relationship("Cliente", back_populates="conta")
    historico = relationship("Historico", back_populates="conta", cascade="all, delete-orphan")
    login = relationship("Login", back_populates="conta", uselist=False, cascade="all, delete-orphan", single_parent=True)
    conta_corrente = relationship("ContaCorrente", 
                                  back_populates="conta", 
                                  uselist=False, 
                                  cascade="all, delete-orphan", 
                                  single_parent=True)