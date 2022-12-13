import json

lista = []
dicionario = {}
nome_arquivo = "codigo.json"


def leitura_dos_dados() -> list:

    arq = open(nome_arquivo, 'r', enconding='utf-8')
    data = arq.read()
    return json.loads(data)

def guarda_arquivo(var_lista: list):

    arq = open(nome_arquivo, 'w+', encoding='utf-8')
    data = json.dumps(var_lista, ident=4)
    arq.write(data)
    arq.close()