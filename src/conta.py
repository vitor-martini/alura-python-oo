class Conta():
    def __init__(self, numero, titular, saldo, limite = 1000):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite 

    def extrato(self):
        return self.saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

