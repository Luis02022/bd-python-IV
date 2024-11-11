import sys
import os 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app_atividade.services.usuario_services  import UsuarioSevices
from app_atividade.repository.usuario_repository import UsuarioRepository
from app_atividade.config.database  import Session

os.system("cls || clear")

def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioSevices(repository)
    while True:
        os.system("cls || clear")
        print("===Senai SOLUTION===")
        print("1- Adicionar usuário")
        print("2- Pesquisar um usuário")
        print("3- Atualizar usuário")
        print("4- Excluir um usuário")
        print("5- Exibir todos os usuários")
        print("0- Sair")
        opcao = int(input("Escolha uma das opções:"))
        
        match(opcao):
            case 1:
                os.system("cls || clear")

                print("|Adicionando usuário|")
                nome = input("Digite seu nome: ")
                email = input("Digite seu email: ")
                senha = input("Digite sua senha: ")

                service.criar_usuario(nome=nome, email=email, senha=senha)
                listar_usuarios = service.listar_todos_usuarios()
                for usuario in listar_usuarios:
                    print(f"\nNome: {usuario.nome} - Email: {usuario.email} - Senha: {usuario.senha}")

                input("Aperte enter para continuar...")
            
            case 2:
                #os.system("cls || clear")
                service.pesquisar_usuario()
                input("Aperte enter para continuar...")            
            case 3:
                os.system("cls || clear")
                service.atualizar_usuario()
                listar_usuarios = service.listar_todos_usuarios()

                for usuario in listar_usuarios:
                    print(f"Nome: {usuario.nome} - Email: {usuario.email} - Senha: {usuario.senha}")

                input("Aperte enter para continuar...")
            
            case 4:
                os.system("cls || clear")
                service.deletar_usuario()
                listar_usuarios = service.listar_todos_usuarios()
                for usuario in listar_usuarios:
                    print(f"\nNome: {usuario.nome} - Email: {usuario.email} - Senha: {usuario.senha}")

                input("Aperte enter para continuar...")
            
            case 5:
                os.system("cls || clear")

                listar_usuarios = service.listar_todos_usuarios()
                for usuario in listar_usuarios:
                    print(f"\nNome: {usuario.nome} - Email: {usuario.email} - Senha: {usuario.senha}")
                input("Aperte enter para continuar...")

            
            case 0:
                break


            case _:
                print("Opção inválida!!")


if __name__ == "__main__":
    main()
