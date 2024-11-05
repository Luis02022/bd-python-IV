import pytest
from ..models.usuario import Usuario

@pytest.fixture
def criar_usuario():
    return Usuario("Luis", "luis@gmail.com","123")


def nome_alterar(criar_usuario):
    assert criar_usuario.nome == "Luis"
    