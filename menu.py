from telas import *
from persistencia import Persistencia


def menu():
    limparTela()
    print("-------- Sistema de Jogadores --------")
    print("1 - Cadastrar Jogador")
    print("2 - Editar Jogador")
    print("3 - Excluir Jogador")
    print("4 - Selecionar Jogador")
    print("5 - Listar Jogadores")
    print("6 - Sair")
    print("-------------------------------------")
    opcao = int(input("Digite a opção desejada: "))
    return opcao


persistencia = Persistencia()

while True:
    opcao = menu()

    if opcao == 1:
        jogador = cadastrarJogador()
        persistencia.criar(jogador)
        exibirMsg("Jogador cadastrado com sucesso!")
    elif opcao == 2:
        jogador = editarJogador()
        persistencia.editar(jogador)
        exibirMsg("Jogador editado com sucesso!")
    elif opcao == 3:
        limparTela()
        id = excluirJogador()
        persistencia.excluir(id)
        exibirMsg("Jogador excluído com sucesso!")
    elif opcao == 4:
        id = selecionarJogador()
        jogador = persistencia.selecionar(id)
        if jogador == None:
            exibirMsg("Jogador não encontrado!")
        else:
            exibirJogador(jogador)
            travarTela()
    elif opcao == 5:
        jogadores = persistencia.selecionar_todos()
        exibirJogadores(jogadores)
    elif opcao == 6:
        break
