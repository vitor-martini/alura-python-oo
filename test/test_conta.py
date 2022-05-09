import sys
import os
import pytest

source_path = os.path.dirname(os.path.abspath("conta.py")) + '\src'
sys.path.insert(1, source_path)
from conta import Conta 

def criar_conta():
    conta = Conta('123', 'Vitor', 1000.0, 5000.0)   
    return conta

def test_saldo():
    conta = criar_conta()
    assert conta.saldo == 1000.0

def test_deposito():
    conta = criar_conta()
    conta.depositar(500)
    assert conta.saldo == 1500.0
    
def test_saque():
    conta = criar_conta()
    conta.sacar(200)
    assert conta.saldo == 800.0 # Sucesso
    with pytest.raises(Exception): # Falha
        conta.sacar(1000)
    
def test_atributos_privados():
    conta = criar_conta()    
    with pytest.raises(AttributeError):
        conta.__numero

def test_transferencia():
    conta_origem = criar_conta()
    conta_destino = criar_conta()

    # Sucesso
    conta_origem.transferir(200, conta_destino)
    assert conta_origem.saldo == 800.0
    assert conta_destino.saldo == 1200.0

    # Falha
    with pytest.raises(Exception):
        conta_origem.transferir(1000, conta_destino)

def test_property_limite():
    conta = criar_conta()
    conta.limite = 10000 
    assert conta.limite == 10000 