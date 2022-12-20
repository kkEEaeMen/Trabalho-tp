from Jogador import Jogador
import os

class teste:
    def cadastrarjogador() -> Jogador:
        teste.limparTela()
        print("====---- Cadastro de Jogadores ----====")
        jogador = Jogador()
        jogador.setNome(input('Nome: '))
        jogador.setMatricula(input('Matricula: '))
        jogador.setTime(input('Time: '))
        jogador.setAltura(float(input('Altura: ')))
        jogador.setPeso(float(input('Peso: ')))

        return jogador


    def editarJogador() -> Jogador:
        teste.limparTela()
        print("====---- Edição de Jogador ----====")
        jogador = Jogador()
        jogador.setNome(input('Nome: '))
        jogador.setMatricula(input('Matricula: '))
        jogador.setTime(input('Time: '))
        jogador.setAltura(float(input('Altura: ')))
        jogador.setPeso(float(input('Peso: ')))

        return jogador


    def excluirJogador():
        print("====---- Exclusão de Jogador ----====")
        teste.limparTela()
        matricula = int(input('Matricula: '))
        return matricula


    def selecionarJogador():
        teste.limparTela()
        print("====---- Seleção de Jogador ----====")
        matricula = int(input('Matricula: '))
        return matricula


    def exibirJogador(jogador: Jogador):
        print("====---- Jogador ----====")
        print(f"Matricula: {jogador.getMatricula()}")
        print(f"Nome: {jogador.getNome()}")
        print(f"Peso: {jogador.getPeso()}")
        print(f"Altura: {jogador.getAltura()}")
        print(f"Time: {jogador.getTime()}")


    def exibirJogadores(jogadores):
        teste.limparTela()
        print("=====-------- Jogadores --------=====")
        for jogadores in jogadores:
            teste.exibirJogadores(jogadores)
        teste.travarTela()


    def limparTela():
        os.system('clear' if os.name == 'posix' else 'cls')


    def travarTela():
        input('Pressione ENTER para continuar...')


    def exibirMsg(msg):
        print(msg)
        teste.travarTela()
