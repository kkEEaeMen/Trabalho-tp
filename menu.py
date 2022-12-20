from telas import *
# from persistencia import *
def menu():
    print(" 1 - cadastrar jogador\n 2 - Excluir jogador por matricula\n 3 - informações de um jogador\n 4 - Mostrar todos o jogadores\n 5 - Editar informações\n 0 - Apagar tudo\n 9 - Sair ")
    opção = int(input("Insira a opção desejada: "))
    return opção

# persistencia = Persistencia()

while True:
    opção = menu()

    if opção == 1:
        teste.cadastrarjogador()

    elif opção == 2:
        teste.excluirJogador()   
    
    elif opção == 3:
        teste.selecionarJogador()
        
    elif opção == 4:
        teste.exibirJogador()   

    elif opção == 5:
        teste.editarJogador()   

    elif opção == 0:
        teste.excluirJogador()   

    else:
        os.system('cls')
        break

        

