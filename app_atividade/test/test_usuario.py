import pytest
from app_atividade.models.usuario import Usuario

    

def teste_nome_vazio():
    with pytest.raises(TypeError, match= "O nome não pode ser vazio"):
        Usuario("","luis@gmail.com","123")

def teste_email_vazio():
    with pytest.raises(TypeError, match= "O email não pode ser vazio"):
         Usuario("Luis","","123")

def teste_senha_vazio():
    with pytest.raises(TypeError, match= "A senha não pode ser vazia"):
        Usuario("Luis","luis@gmail.com","")      