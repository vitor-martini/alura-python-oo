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

    def __str__(self):
        return f'{self.__nome} - {self.ano} - {self.__likes}'

class Filme(Programa):
    def __init__(self, nome, ano, likes, duracao):
        super().__init__(nome, ano, likes)
        self.__duracao = duracao

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.__duracao}min - {self.likes} likes'

class Serie(Programa):
    def __init__(self, nome, ano, likes, temporada):
        super().__init__(nome, ano, likes)
        self.__temporada = temporada

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.__temporada} temporada(s) - {self.likes} likes'

    def __repr__(self):
        return f"Serie('{self.nome}', {self.ano}, {self.likes}, {self.__temporada})"
        
class Playlist:
    def __init__(self, nome, programas):
        self.__nome = nome
        self.programas = programas 

    def __getitem__(self, item):
        return self.programas[item]

    def __len__(self):
        return len(self.programas)