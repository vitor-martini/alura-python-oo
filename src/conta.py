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

    def depositar(self, valor):
        self.__saldo += valor

    def eh_saldo_negativo(self, valor):
        return self.__saldo < valor

    def sacar(self, valor):
        if self.eh_saldo_negativo(valor):
            raise Exception('Saldo indisponível')
        self.__saldo -= valor

    def transferir(self, valor, conta_destino):
        self.sacar(valor)
        conta_destino.depositar(valor)

    def extrato(self):
        print('O saldo da conta "{}" do titular "{}" é de: R${}'.format(self.__numero, self.__titular, self.__saldo))
