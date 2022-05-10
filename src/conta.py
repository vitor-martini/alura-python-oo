class Conta():
    def __init__(self, numero, titular, saldo, limite = 1000):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite 

    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor):
        self.__limite = valor

    @staticmethod
    def codigo_banco():
        return '001'

    def depositar(self, valor):
        self.__saldo += valor

    def __saque_permitido(self, valor):
        valor_disponivel = self.__saldo + self.__limite
        return valor <= valor_disponivel

    def sacar(self, valor):
        if self.__saque_permitido(valor):
            self.__saldo -= valor
        else: 
            raise Exception('Saldo indisponível')

    def transferir(self, valor, conta_destino):
        self.sacar(valor)
        conta_destino.depositar(valor)

    def extrato(self):
        print('O saldo da conta "{}" do titular "{}" é de: R${}'.format(self.__numero, self.__titular, self.__saldo))
