import json
import os.path


class JsonStorage:
    __nome_arquivo = 'dados.json'

    def lerJson(self) -> list[dict]:
        if not os.path.isfile(self.__nome_arquivo):
            self.criarArquivo()

        arq = open(self.__nome_arquivo, 'r', encoding='utf-8')
        data = arq.read()

        if len(data) == 0:
            return []

        data = json.loads(data)
        arq.close()

        return data

    def gravarJson(self, dados: list[dict]) -> None:
        arq = open(self.__nome_arquivo, 'w+', encoding='utf-8')
        data = json.dumps(dados, indent=4)
        arq.write(data)
        arq.close()

    def criarArquivo(self) -> None:
        arq = open(self.__nome_arquivo, 'w+', encoding='utf-8')
        arq.close()
