import sys
import os
from winsound import PlaySound
import pytest

source_path = os.path.dirname(os.path.abspath("programa.py")) + '\\src\\playlist'
sys.path.insert(1, source_path)
from programa import Programa 
from programa import Filme
from programa import Serie
from programa import Playlist

def criar_filme():
    filme = Filme('Vingadores', 2012, 0, 160)   
    return filme

def criar_serie():
    serie = Serie('Cavaleiro da Lua', 2022, 0, 1)
    return serie

def criar_playlist():
    filme = criar_filme()
    serie = criar_serie()
    programas = [filme, serie]
    playlist = Playlist('Programas da Marvel', programas)
    return playlist

def test_nome():
    filme = criar_filme()
    filme.nome = 'Homem Aranha'
    assert filme.nome == 'Homem Aranha'

def test_likes():
    filme = criar_filme()
    filme.dar_likes(3)
    assert filme.likes == 3

def test_str():
    filme = criar_filme()    
    assert str(filme) == 'Vingadores - 2012 - 160min - 0 likes'

def test_polimorfismo():
    filme = criar_filme()
    serie = criar_serie()
    
    playlist = [filme, serie]
    str_filme = 'Vingadores - 2012 - 160min - 0 likes'
    str_serie = 'Cavaleiro da Lua - 2022 - 1 temporada(s) - 0 likes'
    for programa in playlist:
        assert str(programa) == str_filme if type(programa) == Filme else str_serie

def test_repr():
    serie = criar_serie()    
    assert repr(serie) == "Serie('Cavaleiro da Lua', 2022, 0, 1)"

def test_iteracao():
    playlist = criar_playlist()
    str_filme = 'Vingadores - 2012 - 160min - 0 likes'
    str_serie = 'Cavaleiro da Lua - 2022 - 1 temporada(s) - 0 likes'
    for programa in playlist:
        assert str(programa) == str_filme if type(programa) == Filme else str_serie

def test_tamanho():
    playlist = criar_playlist()
    assert len(playlist) == 2
    