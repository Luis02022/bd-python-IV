from models.usuario import Usuario
from sqlalchemy.orm import Session

class UsuarioRepository:
    def __init__(self, session: Session):
        self.session = session


    def salvar_usuario(self, usuario: Usuario):
        