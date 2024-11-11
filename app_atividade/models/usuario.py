from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base 
from ..config.database import db

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key= True, autoincrement= True)
    nome = Column(String(150))
    email = Column(String(150))
    senha = Column(String(150))

    def __init__(self, nome: str, email: str, senha: str):
        self.nome = self._nome_test(nome)
        self.email = self._email_test(email)
        self.senha = self._senha_test(senha)
    

    def _email_test(self, email):
        if not email.strip():
            raise TypeError("O email não pode ser vazio")
        if email != 'luis@gmail.com':
            raise TypeError("Email não existe")
        
        return email
    
    def _senha_test(self, senha):
        if not senha.strip():
            raise TypeError("A senha não pode ser vazia")
        return senha            
    
    def _nome_test(self, nome):
        if not nome.strip():
            raise TypeError("O nome não pode ser vazio")
        
        if nome != 'Luis':
            raise TypeError("Nome inválido do usuario.")
        return nome
    
Base.metadata.create_all(bind=db)