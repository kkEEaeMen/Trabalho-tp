
from main import*

""" 
( ENTIDADE)

JOGADOR DE BASQUETE 

( ATRIBUTOS)

---> MATRICULA
---> NOME
---> TIME
---> ALTURA
---> PESO

"""

while True:

    print(' 1 - cadastrar jogador\n 2 - Excluir jogador por matricula\n 3 - informações de um jogador\n 4 - Mostrar todos o jogadores\n 5 - Editar informações\n 0 - Apagar tudo')
    
    escolha = int(input("Insira a opção desejada: "))
    
    if escolha == 1:

        cadastrar_jogador()
    # elif escolha == 2:

    #     exclui_por_escolha()
    # elif escolha == 3:

    #     selecao_por_matricula()
    # elif escolha == 4:

    #     mostra_todos()
    # elif escolha == 5:

    #     edita_infos()
    # elif escolha == 0:
    #     exclui_tudo()
