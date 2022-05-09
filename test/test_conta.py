import sys
import os
source_path = os.path.dirname(os.path.abspath("conta.py")) + '\src'
sys.path.insert(1, source_path)
from conta import Conta 

def criar_conta():
    conta = Conta('123', 'Vitor', 1000.0, 5000.0)   
    return conta

def test_extrato():
    conta = criar_conta()
    assert conta.extrato() == 1000.0

def test_deposito():
    conta = criar_conta()
    conta.depositar(500)
    assert conta.extrato() == 1500.0
    
def test_saque():
    conta = criar_conta()
    conta.sacar(200)
    assert conta.extrato() == 800.0