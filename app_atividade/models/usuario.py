from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base 
from config.database import db

Base = declarative_base()

class Usario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key= True, autoincrement= True):
    nome = Column(String(150))
    email = Column(String(150))
    senha = Column(String(150))

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


Base.metadata.create_all(bind=db)