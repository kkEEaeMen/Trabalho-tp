import json
from editores import *
import random
from manipulador import *

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
    
    lista_de_jogadores = abre_e_retorna()

    mat = int(input("Insira matricula do jogador que deseja editar as informações:"))
    for i in lista_de_jogadores:
        if i["Matricula"] == mat:
            nome = i["Nome"]
            altura = ["Altura"]
            peso = ["Peso"]
            time = ["time"]
    


# def apaga_infos_do_txt():
#     """ Complemento da função ler_arquivo e mostra_todos. """

#     exclui = open('txt.txt', 'w', encoding='UTF-8')
#     exclui.close()


# def ler_arquivo_txt():
#     """ Complemento da função mostra_todos"""
#     arq1 = open('txt.txt', 'r', encoding='UTF-8')
#     return arq1.read()


# def mostra_todos():
#     """ Função que mostra tudo do arquivo json em uma interface """
    
#     aux = []
#     sg.theme('DarkPurple4')
#     # INSERE NO ARQUIVO TXT
#     lis = abre_e_retorna()
#     for dicionarios in lis:
#         aux.append(str(dicionarios))
#     for dicionarios_em_string in aux:
#         arq_txt = open('txt.txt', 'a', encoding='UTF-8')
#         insere = arq_txt.write(f"\n{dicionarios_em_string}")
#         arq_txt.close()

#     leitura = ler_arquivo_txt()
#     opcoes = [
#         [sg.Text(20*"-=-")],
#         [sg.Text(leitura)],
#         [sg.Button('Voltar')],
#         [sg.Text(20*"-=-")]
#     ]
#     interface = sg.Window("Informações", opcoes)

#     apaga_infos_do_txt()

#     situacoes, escolhas = interface.read()
#     if situacoes == sg.WIN_CLOSED:
#         interface.close()
#     if situacoes == 'Voltar':
#         interface.close()
#         return 0
        


def edita_infos():
    """ A pessoa escolhe o jogador através da matricula acessando as infos que deseja editar."""

    lista_de_jogadores = abre_e_retorna()

    mat = int(input("Insira matricula do jogador que deseja editar as informações:"))
    
    for i in lista_de_jogadores:
        if i["Matricula"] == mat:
                print("1 - Nome\n 2 - Time\n 3 - Altura\n 4 - Peso\n")
                opcao = int(input("Insira a opção desejada"))
                # if opcao == 1:
                #     muda_nome()
                # if opcao == 2:
                #     muda_time()
                # if opcao == 3:
                #     muda_altura()
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
