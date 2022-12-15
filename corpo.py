from PySimpleGUI import PySimpleGUI as sg
import json
from editores import *
from editores import *
import random
from manipulador import *

lista = []
dicionario = {}
nome_arquivo = "codigo.json"

    
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
    
    leitura = abre_e_retorna()
    sg.theme('DarkPurple4')
    opcoes = [
        [sg.Text(20*"-=-")],
        [sg.Text("Insira a matricula do jogador que deseja ver:"), sg.Input(key='insira_mat')],
        [sg.Button('Confirmar')],
        [sg.Text(20*"-=-")]
    ]
    interface = sg.Window("Busca", opcoes)

    botoes, keys = interface.read()

    for chave, valor in keys.items():
        mat = valor
    if botoes == 'Confirmar':
        for i in leitura:
            if i["Matricula"] == mat:
                interface.close()
                sg.theme('DarkPurple4')
                interface2 = [
                    [sg.Text(20*"-=-")],
                    [sg.Text(i)],
                    [sg.Button('Voltar')],
                    [sg.Text(20*"-=-")]
                ]
                inter = sg.Window("Informações", interface2)
                botoes2, keys2 = inter.read()
                if botoes2 == 'Voltar':
                    inter.close()
                    return "Encontrado"
    
    sg.theme('Black')
    interface3 = [
        [sg.Text(20*"-=-")],
        [sg.Text('Jogador não encontrado.\nPor favor tente outra matricula !')],
        [sg.Button('Voltar')],
        [sg.Text(20*"-=-")]
    ]
    interf = sg.Window("Erro !", interface3)
    b2, k2 = interf.read()
    if b2 == 'Voltar':
        interface.close()
        interf.close()
        return "Não encontrado"
            
    
def apaga_infos_do_txt():
    """ Complemento da função ler_arquivo e mostra_todos. """

    exclui = open('txt.txt', 'w', encoding='UTF-8')
    exclui.close()


def ler_arquivo_txt():
    """ Complemento da função mostra_todos"""
    arq1 = open('txt.txt', 'r', encoding='UTF-8')
    return arq1.read()


def mostra_todos():
    """ Função que mostra tudo do arquivo json em uma interface """
    
    aux = []
    sg.theme('DarkPurple4')
    # INSERE NO ARQUIVO TXT
    lis = abre_e_retorna()
    for dicionarios in lis:
        aux.append(str(dicionarios))
    for dicionarios_em_string in aux:
        arq_txt = open('txt.txt', 'a', encoding='UTF-8')
        insere = arq_txt.write(f"\n{dicionarios_em_string}")
        arq_txt.close()

    leitura = ler_arquivo_txt()
    opcoes = [
        [sg.Text(20*"-=-")],
        [sg.Text(leitura)],
        [sg.Button('Voltar')],
        [sg.Text(20*"-=-")]
    ]
    interface = sg.Window("Informações", opcoes)

    apaga_infos_do_txt()

    situacoes, escolhas = interface.read()
    if situacoes == sg.WIN_CLOSED:
        interface.close()
    if situacoes == 'Voltar':
        interface.close()
        return 0
        

def menu_da_edicao(dicionario_do_jogador: dict, matricula_inserida):
    """ Complemento da função edita infos."""

    lista_de_matriculas = abre_e_retorna()
    opcoes2 = [
                [sg.Text(20*"-=-")],
                [sg.Button('(1) - Nome')],
                [sg.Button('(2) - Altura')],
                [sg.Button('(3) - Time')],
                [sg.Button('(4) - Peso')],
                [sg.Text(20*"-=-")]
                ]
    interface1 = sg.Window("Edição", opcoes2)
    opc1, opc2 = interface1.read()
    opcao_escolhida2 = opc1


    if opc1 == ('(1) - Nome'):
        interface1.close()
        muda_nome(dicionario_do_jogador)
    if opc1 == ('(2) - Altura'):
        interface1.close()
        muda_altura (dicionario_do_jogador)
    if opc1 == ('(3) - Time'):
        interface1.close()
        muda_time(dicionario_do_jogador)
    if opc1 == ('(4) - Peso'):
        interface1.close()
        muda_peso(dicionario_do_jogador)


def edita_infos():
    """ A pessoa escolhe o jogador através da matricula acessando as infos do mesmo para edição."""

    lista_de_jogadores = abre_e_retorna()
    opcoes = [
        [sg.Text(20*"-=-")],
        [sg.Text("Insira matricula do jogador que deseja editar as informações:"), sg.Input(key= ('mat'))],
        [sg.Button('Confirmar')],
        [sg.Text(20*"-=-")]
    ]
    interface = sg.Window("Edição", opcoes)
    op1, op2 = interface.read()

    # OP2 E RETORNADO EM DICIONARIO E 
    # EU PRECISO PEGAR O VALOR INSERIDO
    for chave, matricula_do_jogador in op2.items():
        if op1 == 'Confirmar':
            for i in lista_de_jogadores:

                matri = matricula_do_jogador

                if i["Matricula"] == matri:
                    interface.close()
                    menu_da_edicao(i,matri)
                    return 0 

    sg.theme('Black')
    interface3 = [
        [sg.Text(20*"-=-")],
        [sg.Text('Jogador não encontrado.\nPor favor tente outra matricula !')],
        [sg.Button('Voltar')],
        [sg.Text(20*"-=-")]
    ]
    interf = sg.Window("Erro !", interface3)
    b2, k2 = interf.read()
    if b2 == 'Voltar':
        interface.close()
        interf.close()
        return "Não encontrado"


def exclui_por_escolha():
    lis = abre_e_retorna()
    pass
    


def cadastrar_jogador():
    """ Função para cadastrar jogadores no arquivo json."""
        
        dicionario["Matricula"] = input("Insira um valor: ")
        dicionario["Nome"] = input("Insira o nome do jogador: ")
        dicionario["Altura"] = input("Insira a altura do jogador: ")
        dicionario["time"] = input("Insira o time do jogador: ")
        dicionario["Peso"] = input("Insira o peso do jogador: ")
