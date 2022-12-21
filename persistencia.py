from json_storage import *
from Jogador import *


class Persistencia():
    __storage = JsonStorage()

    def criar(self, dado: JsonStorage) -> Jogador:
        dados = self.selecionar_todos()
        dado.setMatricula(self.__gerarMatricula())
        dados.append(dado)
        self.__storage.gravarJson(list(map(lambda x: x.toDict(), dados)))

    def editar(self, dado: JsonStorage) -> None:
        dados = self.selecionar_todos()
        for i, data in enumerate(dados):
            if data.getMatricula() == dado.getMatricula():
                dados[i] = dado
        self.__storage.gravarJson(list(map(lambda x: x.toDict(), dados)))

    def excluir(self, matricula: int) -> None:
        dados = self.selecionar_todos()
        for dado in dados:
            if dado.getMatricula() == matricula:
                dados.remove(dado)
        self.__storage.gravarJson(list(map(lambda x: x.toDict(), dados)))

    def selecionar(self, matricula: int) -> Jogador | None:
        dados = self.selecionar_todos()
        for dado in dados:
            if dado.getMatricula() == matricula:
                return dado
        return None

    def selecionar_todos(self) -> list[Jogador]:
        jogadores = []
        for i in self.__storage.lerJson():
            jogador = Jogador()
            jogador.setNome(i['nome'])
            jogador.setPeso(i['peso'])
            jogador.setAltura(i['altura'])
            jogador.setTime(i['time'])
            jogador.setMatricula(i['matricula'])
            jogadores.append(jogador)
        return jogadores

    def __gerarMatricula(self) -> int:
        dados = self.selecionar_todos()
        if len(dados) == 0:
            return 1
        return dados[-1].getMatricula() + 1

