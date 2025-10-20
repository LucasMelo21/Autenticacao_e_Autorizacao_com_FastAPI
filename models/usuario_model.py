from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from core.configs import settings

class UsuarioModel(settings.DBBaseModel):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=True)
    sobrenome = Column(String(100), nullable=True)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False, unique=True)
    eh_admin = Column(Boolean, default=False)
    artigos = relationship(
        "ArtigoModel",
        cascade="all, delete-orphan",
        back_populates="criador",
        uselist=True,
        lazy="joined")