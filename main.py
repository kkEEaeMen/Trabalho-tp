from random import *

lista = []
dicionario = {}


def cadastrar_jogador():
    dicionario["Matricula"] = randint(0,100)
    print(dicionario["Matricula"])