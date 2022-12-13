class Jogador:
    __nome: str
    __altura: float
    __peso: float
    __matricula: int

    def setNome(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome

    def setAltura(self, altura):
        self.__altura = altura

    def getAltura(self):
        return self.__altura

    def setPeso(self, Peso):
        self.__peso = Peso

    def getPeso(self):
        return self.__peso

    def setMatricula(self, matricula):
        self.__matricula = matricula

    def getMatricula(self):
        return self.__matricula
 
    def interface(self):
        return f"O {self.__nome} é gente boa !"

jogador = Jogador()








