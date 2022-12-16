import json
from json_storage import *
from edits import *
from modelagem import *
from telas import *
import os
import random

lista = []
dicionario = {}

def exclui_tudo():
    """ Exclui tudo de dentro do json"""

    pergunta = input("Deseja excluir tudo ? (s/n)\n").lower()
    
    if pergunta == 's':
        dicii = []
        arq = open(nome_arquivo, 'w', encoding='UTF-8')
        data = json.dumps(dicii)
        arq.write(data)
        arq.close
    
def selecao_por_matricula():
    """ Imprime as informações de um jogador buscado pela matricula """ 
    os.system('cls')
    lista_de_jogadores = abre_e_retorna()

    mat = int(input("Insira matricula do jogador que deseja editar as informações:"))
    for i in lista_de_jogadores:
        if i["Matricula"] == mat:
            set(i["Matricula"], i["Nome"], i["Altura"], i["Peso"], i["time"])
            os.system('cls')
            print(mostra.imprimeJogadores())
            print(input("Aperte ENTER para continuar... "))

def mostra_todos():
    os.system('cls')
    lista_de_jogadores = abre_e_retorna()

    for i in range(len(lista_de_jogadores)):
        set(lista_de_jogadores[i]["Matricula"], lista_de_jogadores[i]["Nome"], lista_de_jogadores[i]["Altura"], lista_de_jogadores[i]["Peso"], lista_de_jogadores[i]["time"])
        print(mostra.imprimeJogadores())
        print(10*"--==")
    
    print(input("Aperte ENTER para continuar... "))

def edita_infos():
    """ A pessoa escolhe o jogador através da matricula acessando as infos que deseja editar."""

    lista_de_jogadores = abre_e_retorna()

   
    print(" 1 - Nome\n 2 - Time\n 3 - Altura\n 4 - Peso\n")
    opcao = int(input("Insira a opção desejada: "))
    # if opcao == 1:
    #     muda_nome()
    # if opcao == 2:
    #     muda_time()
    if opcao == 3:
        muda_altura()
    # if opcao == 4:
    #     muda_peso()

# def exclui_por_escolha():
#     lis = abre_e_retorna()
#     pass


def cadastrar_jogador():
        
    infos = abre_e_retorna()

    dicionario["Matricula"] = random.randint(1,100)
    dicionario["Nome"] = input("Insira o nome do jogador: ")
    dicionario["Altura"] = input("Insira a altura do jogador: ")
    dicionario["time"] = input("Insira o time do jogador: ")
    dicionario["Peso"] = input("Insira o peso do jogador: ")

    infos.append(dicionario)
    guarda_arquivo(infos)
    os.system('cls')
    print(10 * "--==")
    print(" A matricula gerada foi:",dicionario["Matricula"],"\n Favor guardar a matricula.")
    print(10 * "--==")
    print(input("Aperte ENTER para voltar ao menu... "))