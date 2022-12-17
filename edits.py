from json_storage import *


def muda_nome():
    """ Função para substituição do nome."""

    leitura = abre_e_retorna()
    mat = int(input("Insira matricula do jogador que deseja editar as informações:"))
    for jogador in leitura:
        if jogador["Matricula"] == mat:
            valor = input("Insira um novo nome: ")
            for nome in leitura:
                nome["Nome"] = valor

    guarda_arquivo(leitura)
    input("Pressione ENTER para voltar ao menu")
    guarda_arquivo(leitura)
     

def muda_altura ():
    """ Função para substituição do Altura."""

    leitura = abre_e_retorna()
    mat = int(input("Insira matricula do jogador que deseja editar as informações:"))
    for jogador in leitura:
        if jogador["Matricula"] == mat:
            valor = input("Insira um novo valor: ")
            for altura in leitura:
                altura["Altura"] = valor

    guarda_arquivo(leitura)
    input("Pressione ENTER para voltar ao menu")
    guarda_arquivo(leitura)


def muda_time():
    """ Função para substituição do Time."""

    leitura = abre_e_retorna()
    mat = int(input("Insira matricula do jogador que deseja editar as informações:"))
    for jogador in leitura:
        if jogador["Matricula"] == mat:
            valor = input("Insira um novo valor: ")
            for time in leitura:
                time["Time"] = valor
                
    guarda_arquivo(leitura)
    input("Pressione ENTER para voltar ao menu")
    guarda_arquivo(leitura)


def muda_peso():
    """ Função para substituição do Peso."""

    leitura = abre_e_retorna()
    mat = int(input("Insira matricula do jogador que deseja editar as informações:"))
    for jogador in leitura:
        if jogador["Matricula"] == mat:
            valor = input("Insira um novo valor: ")
            for peso in leitura:
                peso["Peso"] = valor

    guarda_arquivo(leitura)
    input("Pressione ENTER para voltar ao menu")
    guarda_arquivo(leitura)


def excluir_por_escolha():
    """ Função para excluir por matricula."""

    leitura = abre_e_retorna()
    mat = int(input("Insira matricula do jogador que deseja apagar as informações:"))
    for jogador in leitura:
        if jogador["Matricula"] == mat:
            indice = leitura.index(jogador)
            leitura.pop(indice)
    guarda_arquivo(leitura)
    print(10*"-=-=-")
    print("Informações do jogador apagadas com sucesso")
    print(10*"-=-=-")

            
    input("Pressione ENTER para voltar ao menu")

            




            

