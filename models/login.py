from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey

from db.setup import Base

class Login(Base):
    __tablename__ = "login"
    id_conta_login = Column(Integer, ForeignKey("conta.id"), primary_key=True)
    senha = Column(String(255), nullable=False)

    conta = relationship("Conta", back_populates="login", uselist=False)