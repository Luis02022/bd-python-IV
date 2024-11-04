from services.usuario_services  import UsuarioSevices
from repository.usuario_repository import UsuarioRepository
from config.database  import Session
import os 

os.system("cls || clear")

def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioSevices(repository)
    
    print("|Adicionando usuário|")
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    service.criar_usuario(nome=nome, email=email, senha=senha)
    listar_usuarios = service.listar_todos_usuarios()
    for usuario in listar_usuarios:
        print(f"Nome: {usuario.nome} - Email: {usuario.email} - Senha: {usuario.senha}")

    service.deletar_usuario()
    
    

    listar_usuarios = service.listar_todos_usuarios()
    for usuario in listar_usuarios:
        print(f"Nome: {usuario.nome} - Email: {usuario.email} - Senha: {usuario.senha}")


if __name__ == "__main__":
    main()
