class Programa():
    def __init__(self, nome, ano, likes):
        self.__nome = nome
        self.ano = ano
        self.__likes = likes

    @property
    def likes(self):
        return self.__likes

    def dar_likes(self, quantidade = 1):
        self.__likes += quantidade

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

class Filme(Programa):
    def __init__(self, nome, ano, likes, duracao):
        super().__init__(nome, ano, likes)
        self.duracao = duracao

class Serie(Programa):
    def __init__(self, nome, ano, likes, temporada):
        super().__init__(nome, ano, likes)
        self.temporada = temporada

    