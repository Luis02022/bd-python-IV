from models.usuario import Usuario
from repository.usuario_repository import UsuarioRepository


class UsuarioSevices:
    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

    def criar_usuario(self, nome: str, email: str, senha: str):
        try:
            usuario = Usuario(nome=nome, email=email, senha=senha)

            novo_usuario = self.repository.pesquisar_usuario_por_email(usuario.email)

            if novo_usuario:
                print("Usuário já cadastrado!")
                return

            self.repository.salvar_usuario(usuario)
            print("Usuário cadastrado com sucesso!!")
        except TypeError as erro:
            print(f"Erro ao salvar o usuário: {erro}")
        except ValueError as erro:
            print(f"Ocorreu um erro inesperado: {erro}")

    def deletar_usuario(self):
        try:
            email_delete = input("Digite um email que deseja excluir:")

            usuario = self.repository.pesquisar_usuario_por_email( email= email_delete)

            if usuario:
                self.repository.excluir_usuario(usuario)
                print("Usuário excluido com sucesso!")
                input("Aperte enter para continuar...")
                return

            print("Usuario não encontrado.")
            input("Aperte enter para continuar...")

        except TypeError as erro:
            print(f"Erro ao excluir usuário: {erro}")
        except ValueError as erro:
            print(f"Ocorreu um erro inesperado ao excluir: {erro}")

    def listar_todos_usuarios(self):
        return self.repository.listar_usuario()
