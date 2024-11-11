import pytest
from ..models.usuario import Usuario



@pytest.fixture
def criar_usuario():
    return Usuario("Luis","luis@gmail.com","123")


def test_nome_alterar(criar_usuario):
    assert criar_usuario.nome == "Luis"
    

def teste_nome_vazio():
    with pytest.raises(TypeError, match= "O nome não pode ser vazio"):
        Usuario("","luis@gmail.com","123")

def test_nome_invalido():
    with pytest.raises(TypeError, match = "Nome inválido do usuario."):
        Usuario("Mario","luis@gmail.com","123")

def teste_email_vazio():
    with pytest.raises(TypeError, match= "O email não pode ser vazio"):
         Usuario("Luis","","123")

def teste_email_invalido():
    with pytest.raises(TypeError, match= "Email não existe"):
        Usuario("Luis","luisinho@gmail.com","123")

def teste_senha_vazio():
    with pytest.raises(TypeError, match= "A senha não pode ser vazia"):
        Usuario("Luis","luis@gmail.com","")      
