from PySimpleGUI import PySimpleGUI as sg
import json
from complemento import *

lista = []
dicionario = {}
nome_arquivo = "codigo.json"


def abre_e_retorna() -> list:
    """Abre json para edição por leitura, devolvendo uma lista."""

    arq = open(nome_arquivo, 'r', encoding='utf-8')
    data = arq.read()
    return json.loads(data)

def guarda_arquivo(var_lista: list):
    

    arq = open(nome_arquivo, 'w+', encoding='utf-8')
    data = json.dumps(var_lista, indent=4)
    arq.write(data)
    arq.close()
    sg.theme('DarkBlue16')
    mensagem_de_conclusao = [

            [sg.Text(20*"-=-")],
            [sg.Text("As informações foram salvas com sucesso !")],
            [sg.Button('Confirmar')],
            [sg.Text(20*"-=-")]
                                ]
    conclusao_tela = sg.Window("Conclusão", mensagem_de_conclusao)
    b, c = conclusao_tela.read()
    if b == 'Confirmar':
        conclusao_tela.close()
        return 'Confirmar'
    

def exclui_tudo():
    """ Exclui tudo de dentro do json"""

    opcoes = [
        [sg.Text(20*"-=-")],
        [sg.Text("Deseja realmente apagar todas as matriculas ")],
        [sg.Button('Sim'),sg.Button('Não')],
        [sg.Text(20*"-=-")]
    ]
    tela = sg.Window("Deletar", opcoes)
    ch, ky = tela.read()
    if ch == 'Sim':
        tela.close()
        dicii = []
        arq = open(nome_arquivo, 'w', encoding='UTF-8')
        data = json.dumps(dicii)
        arq.write(data)
        arq.close
    else:
        tela.close()
        return 0 


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
  
    sg.theme('DarkPurple4')
    interface_de_opcao_invalida = [
        [sg.Text(20*"-=-")],
        [sg.Text("Insira matricula do jogador que deseja excluir"), sg.Input(key= ('mat'))],
        [sg.Button('Confirmar')],
        [sg.Text(20*"-=-")]
    ]
    interface2 = sg.Window("Busca", interface_de_opcao_invalida)
    botao, keys = interface2.read()
    for chave, valor in keys.items():
        matri = valor
    if botao == 'Confirmar':
        interface2.close()
        for elementos in lis:
            if elementos["Matricula"] == matri:
                posicao = lis.index(elementos)
                lis.pop(posicao)
                guarda_arquivo(lis)
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
        interf.close()
        interface2.close()
        return "Não encontrado"


def cadastrar_jogador():
    """ Função para cadastrar jogadores no arquivo json."""


    sg.theme('DarkPurple4')

    opcoes = [
        [sg.Text(20*"-=-")],
        [sg.Text('1 - Insira um valor para matricula: '),
         sg.Input(key='Código', size=(20, 2))],
        [sg.Text('2 - Nome do jogador(a): '),
         sg.Input(key='Identidade', size=(20, 2))],
        [sg.Text('3 - Altura do jogador(a) em CM:'),
         sg.Input(key='Tamanho', size=(20, 2))],
        [sg.Text('4 - Time do jogador(a):'),
         sg.Input(key='Equipe', size=(20, 2))],
        [sg.Text('5 - Insira o peso do jogador(a) em KG:'),
         sg.Input(key='KG', size=(20, 2))],
        [sg.Button("Confirmar")],
        [sg.Text(20*"-=-")]
    ]

    interface = sg.Window("Tela de cadastro", opcoes)

    while True:
        situacoes, escolhas = interface.read()
        if situacoes == sg.WIN_CLOSED:
            break

        dicionario["Matricula"] = escolhas['Código']
        dicionario["Nome"] = escolhas['Identidade']
        dicionario["Altura"] = escolhas['Tamanho']
        dicionario["time"] = escolhas['Equipe']
        dicionario["Peso"] = escolhas['KG']
        
        var_lista = abre_e_retorna()

        for verifica_campos1, verifica_campos2 in dicionario.items():
            if verifica_campos2 == "":
                sg.theme('Black')
                mensag_de_erro = [

                [sg.Text(20*"-=-")],
                [sg.Text("Você não pode deixar campos vazios !")],
                [sg.Button('Confirmar')],
                [sg.Text(20*"-=-")]
                                    ]
                tela_de_verificacao = sg.Window("Erro !", mensag_de_erro)
                bton, ky = tela_de_verificacao.read()
                if bton == 'Confirmar':
                    interface.close()
                    tela_de_verificacao.close()
                    return 0

        for verifica_matricula in var_lista:
            if verifica_matricula["Matricula"] == dicionario["Matricula"]:
                sg.theme('Black')
                mensagem_de_erro = [

                [sg.Text(20*"-=-")],
                [sg.Text("Essa matricula ja existe, favor inserir outra ! !")],
                [sg.Button('Confirmar')],
                [sg.Text(20*"-=-")]
                                    ]
                tela_de_verificacao2 = sg.Window("Erro !", mensagem_de_erro)
                btton, kys = tela_de_verificacao2.read()
                if btton == 'Confirmar':
                    interface.close()
                    tela_de_verificacao2.close()
                    return 0

        var_lista.append(dicionario)
        guarda_arquivo(var_lista)
        interface.close()
