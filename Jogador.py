class Jogador:
    __nome: str
    __altura: float
    __peso: float
    __matricula: int
    __time: str

    def setMatricula(self, matricula):
        self.__matricula = matricula

    def getMatricula(self):
        return self.__matricula

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

    def setTime(self, time):
        self.__time = time

    def getTime(self):
        return self.__time


    def toDict(self):
        return {
            "Matricula": self.__matricula,
            "Nome": self.__nome,
            "Peso": self.__peso,
            "Altura": self.__altura,
            "Time": self.__time
        }






