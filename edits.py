from json_storage import *

# def muda_nome(dicionario_do_jogador: dict):
#     """ Função para substituição do nome."""

#     leitura = abre_e_retorna()
#     for dicts in range(len(leitura)):
#         if leitura[dicts] == dicionario_do_jogador:
#             sg.theme('DarkPurple3')
            
#             opcoes = [

#             [sg.Text(20*"-=-")],
#             [sg.Text("Insira o nome para substituição:"), sg.Input(key= ('nome_substituto'))],
#             [sg.Button('Confirmar')],
#             [sg.Text(20*"-=-")]
#                                 ]
#             interface_nome = sg.Window("Edição", opcoes)
#             botoes, keys = interface_nome.read()

#     for chave, valor in keys.items():
#         for i in leitura:
#             if i == dicionario_do_jogador:
#                 i["Nome"] = valor
#                 interface_nome.close()

#     guarda_arquivo(leitura)
            
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



    guarda_arquivo(leitura) # n sei se funciona, tem que ver se tem que fazer algo

# def muda_time(dicionario_do_jogador: dict):
#     """ Função para substituição do Time."""

#     leitura = abre_e_retorna()
#     for dicts in range(len(leitura)):
#         if leitura[dicts] == dicionario_do_jogador:
#             sg.theme('DarkPurple3')
            
#             opcoes = [
                
#             [sg.Text(20*"-=-")],
#             [sg.Text("Insira o nome do time para substituição:"), sg.Input(key= ('nome_substituto'))],
#             [sg.Button('Confirmar')],
#             [sg.Text(20*"-=-")]
#                                 ]
#             interface_time = sg.Window("Edição", opcoes)
#             botoes, keys = interface_time.read()
#     for chave, valor in keys.items():
#         for i in leitura:
#             if i == dicionario_do_jogador:
#                 i["time"] = valor
#                 interface_time.close()
#     guarda_arquivo(leitura)


# def muda_peso(dicionario_do_jogador: dict):
#     """ Função para substituição do Peso."""

#     leitura = abre_e_retorna()
#     for dicts in range(len(leitura)):
#         if leitura[dicts] == dicionario_do_jogador:
#             sg.theme('DarkPurple3')
            
#             opcoes = [
                
#             [sg.Text(20*"-=-")],
#             [sg.Text("Insira o novo peso para substituição:"), sg.Input(key= ('nome_substituto'))],
#             [sg.Button('Confirmar')],
#             [sg.Text(20*"-=-")]
#                                 ]
#             interface_peso = sg.Window("Edição", opcoes)
#             botoes, keys = interface_peso.read()
#     for chave, valor in keys.items():
#         for i in leitura:
#             if i == dicionario_do_jogador:
#                 i["Peso"] = valor
#                 interface_peso.close()
#     guarda_arquivo(leitura)
            

