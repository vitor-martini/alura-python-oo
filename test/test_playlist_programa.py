import sys
import os
import pytest

source_path = os.path.dirname(os.path.abspath("programa.py")) + '\\src\\playlist'
sys.path.insert(1, source_path)
from programa import Programa 
from programa import Filme
from programa import Serie

def criar_filme():
    filme = Filme('Vingadores', 2012, 0, 160)   
    return filme

def criar_serie():
    serie = Serie('Cavaleiro da Lua', 2022, 0, 1)
    return serie

def test_nome():
    filme = criar_filme()
    filme.nome = 'Homem Aranha'
    assert filme.nome == 'Homem Aranha'

def test_likes():
    filme = criar_filme()
    filme.dar_likes(3)
    assert filme.likes == 3