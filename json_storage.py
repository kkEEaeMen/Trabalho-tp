import json
import os

class JsonStorage:
    __nome_arquivo = "dados.json"

def abre_e_retorna() -> list:
    """ Abre json para edição por leitura, devolvendo uma lista."""

    arq = open(JsonStorage.__nome_arquivo, 'r', encoding='utf-8')
    data = arq.read()
    return json.loads(data)


def guarda_arquivo(var_lista: list):
    
    arq = open(JsonStorage.__nome_arquivo, 'w+', encoding='utf-8')
    data = json.dumps(var_lista, indent=4)
    arq.write(data)
    arq.close()

    