from app_atividade.models.usuario import Usuario
from app_atividade.repository.usuario_repository import UsuarioRepository


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

    def listar_todos_usuarios(self):
        return self.repository.listar_usuario()

    
    def deletar_usuario(self):
        try:
            email_delete = input("Digite um email que deseja excluir:")

            usuario = self.repository.pesquisar_usuario_por_email(email=email_delete)

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

    def atualizar_usuario(self):
        try:
            print("Atualizando dados do usuário;")

            email_usuario = input("Informe o email do usuário:")

            usuario_cadastrado = self.repository.pesquisar_usuario_por_email(email= email_usuario)

            if usuario_cadastrado:
                usuario_cadastrado.nome = input("Digite seu nome:")
                usuario_cadastrado.email = input("Digite seu email:")
                usuario_cadastrado.senha = input("Digite sua senha:")
                self.repository.atualizar_dados_usuario(usuario_cadastrado)
                return 
            else:
                print("Usuário não encontrado.")

        except TypeError as erro:
            print(f"Erro ao atualizar o usuário: {erro}")
        except ValueError as erro:
            print(f"Ocorreu um erro inesperado: {erro}")

    def pesquisar_usuario(self):
        try:
            nome_pesquisar = input("Digite o nome que você deseja pesquisar: ")
            usuario = self.repository.pesquisar_usuario_por_email(nome_pesquisar)
            if usuario:
                print(f"{usuario.id} - {usuario.nome} - {usuario.email} - {usuario.senha}")
                return
            print("Usuario não encontrado!")
        
        except TypeError as erro:
            print(f"Erro ao salvar usuário: {erro}")
        except Exception as erro:
            print (f"ocorreu um erro inesperado: {erro}")