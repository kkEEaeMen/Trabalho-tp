class Jogador:
    __nome: str
    __altura: float
    __peso: float
    __matricula: int

    def setNome(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome

    def interface(self):
        return f"O {self.__nome} é gente boa !"



produto = Produto()