import json
from PySimpleGUI import PySimpleGUI as sg
from manipulador import *

<<<<<<< HEAD:complemento.py

def leitura_2() -> list:
    """ Abre json para edição por leitura, devolvendo uma lista."""

    arquivo = open('codigo.json', 'r', encoding='utf-8') 
    data = arquivo.read()
    return json.loads(data)

def salva_substituicao(leitura: list):
    """ Subistitui os cadastros de dentro do json pelos editados."""

    arquivo = open('codigo.json', 'w+', encoding='utf-8')
    data = json.dumps(leitura, indent=4)
    arquivo.write(data)
    arquivo.close()
    sg.theme('DarkBlue16')
    mensagem_de_conclusao = [

            [sg.Text(20*"-=-")],
            [sg.Text("A edição foi concluida com êxito !")],
            [sg.Button('Confirmar')],
            [sg.Text(20*"-=-")]
                                ]
    conclusao_tela = sg.Window("Edição", mensagem_de_conclusao)
    b, c = conclusao_tela.read()
    if b == 'Confirmar':
        conclusao_tela.close()
        return 'Confirmar'

    
=======
>>>>>>> 81f07dd31ed3f7769099bffab0a9f1a5670336fc:editores.py
def muda_nome(dicionario_do_jogador: dict):
    """ Função para substituição do nome."""

    leitura = abre_e_retorna()
    for dicts in range(len(leitura)):
        if leitura[dicts] == dicionario_do_jogador:
            sg.theme('DarkPurple3')
            
            opcoes = [

            [sg.Text(20*"-=-")],
            [sg.Text("Insira o nome para substituição:"), sg.Input(key= ('nome_substituto'))],
            [sg.Button('Confirmar')],
            [sg.Text(20*"-=-")]
                                ]
            interface_nome = sg.Window("Edição", opcoes)
            botoes, keys = interface_nome.read()

    for chave, valor in keys.items():
        for i in leitura:
            if i == dicionario_do_jogador:
                i["Nome"] = valor
                interface_nome.close()

                

    guarda_arquivo(leitura)
            

def muda_altura (dicionario_do_jogador: dict):
    """ Função para substituição do Altura."""

    leitura = abre_e_retorna()
    for dicts in range(len(leitura)):
        if leitura[dicts] == dicionario_do_jogador:
            sg.theme('DarkPurple3')
            
            opcoes = [
                
            [sg.Text(20*"-=-")],
            [sg.Text("Insira um nome para substituição:"), sg.Input(key= ('nome_substituto'))],
            [sg.Button('Confirmar')],
            [sg.Text(20*"-=-")]
                                ]
            interface_altura = sg.Window("Edição", opcoes)
            botoes, keys = interface_altura.read()

    for chave, valor in keys.items():
        for i in leitura:
            if i == dicionario_do_jogador:
                i["Altura"] = valor
                interface_altura.close()

    guarda_arquivo(leitura)

def muda_time(dicionario_do_jogador: dict):
    """ Função para substituição do Time."""

    leitura = abre_e_retorna()
    for dicts in range(len(leitura)):
        if leitura[dicts] == dicionario_do_jogador:
            sg.theme('DarkPurple3')
            
            opcoes = [
                
            [sg.Text(20*"-=-")],
            [sg.Text("Insira o nome do time para substituição:"), sg.Input(key= ('nome_substituto'))],
            [sg.Button('Confirmar')],
            [sg.Text(20*"-=-")]
                                ]
            interface_time = sg.Window("Edição", opcoes)
            botoes, keys = interface_time.read()
    for chave, valor in keys.items():
        for i in leitura:
            if i == dicionario_do_jogador:
                i["time"] = valor
                interface_time.close()
    guarda_arquivo(leitura)


def muda_peso(dicionario_do_jogador: dict):
    """ Função para substituição do Peso."""

    leitura = abre_e_retorna()
    for dicts in range(len(leitura)):
        if leitura[dicts] == dicionario_do_jogador:
            sg.theme('DarkPurple3')
            
            opcoes = [
                
            [sg.Text(20*"-=-")],
            [sg.Text("Insira o novo peso para substituição:"), sg.Input(key= ('nome_substituto'))],
            [sg.Button('Confirmar')],
            [sg.Text(20*"-=-")]
                                ]
            interface_peso = sg.Window("Edição", opcoes)
            botoes, keys = interface_peso.read()
    for chave, valor in keys.items():
        for i in leitura:
            if i == dicionario_do_jogador:
                i["Peso"] = valor
                interface_peso.close()
    guarda_arquivo(leitura)
            

