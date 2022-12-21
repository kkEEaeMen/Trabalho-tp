import os
from Jogador import Jogador


def cadastrarJogador() -> Jogador:
    limparTela()
    print("-------- Cadastro de Produto --------")
    jogador = Jogador()
    jogador.setNome(input('Nome: '))
    jogador.setTime(input('Time: '))
    jogador.setAltura(float(input('Altura: ')))
    jogador.setPeso(float(input('Peso: ')))

    return jogador


def editarJogador() -> Jogador:
    limparTela()
    print("-------- Edição de Jogador --------")
    jogador = Jogador()
    jogador.setNome(input('Nome: '))
    jogador.setMatricula(input('Matricula: '))
    jogador.setTime(input('Time: '))
    jogador.setAltura(float(input('Altura: ')))
    jogador.setPeso(float(input('Peso: ')))



def excluirJogador():
    print("-------- Exclusão de Jogador --------")
    limparTela()
    matricula = int(input('Matricula: '))
    return matricula


def selecionarJogador():
    limparTela()
    print("-------- Seleção de Jogador --------")
    matricula = int(input('Matricula: '))
    return matricula


def exibirJogador(jogador: Jogador):
    print("-------- Jogador --------")
    print(f"Matricula: {jogador.getMatricula()}")
    print(f"Nome: {jogador.getNome()}")
    print(f"Peso: {jogador.getPeso()}")
    print(f"Altura: {jogador.getAltura()}")
    print(f"Time: {jogador.getTime()}")


def exibirJogadores(jogadores):
    limparTela()
    print("---------------- Jogadores ----------------")
    for jogador in jogadores:
        exibirJogador(jogador)
    travarTela()


def limparTela():
    os.system('clear' if os.name == 'posix' else 'cls')


def travarTela():
    input('Pressione ENTER para continuar...')


def exibirMsg(msg):
    print(msg)
    travarTela()
