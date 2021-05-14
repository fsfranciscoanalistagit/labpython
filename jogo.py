import random

class AnalisarJogada:
    """Objetivo: fazer jogo da velha: jogo manual e automático
    - criar uma lista com todas as posições de jogada - tabuleiro
    - alternar entre dois jogadores e diferenciar suas jogadas com uma letra na posição de jogo escolhida
    - pedir a posição de jogada e mostrar na tela o tabuleiro
    - parar o jogo quando um dos jogadores vencer e informar o vencedor
    - jogador altomático ou jogador pc:
        - defesa: de 3 posição do tabuleiro, se duas estiver jogada pelo oponente
          deve realizar a terceira, fazendo o bloqueio para não marcar ponto
        - ataque intermediário: verificar duas posições marcada para marcar a terceira
        - ataque experiente: verificar posição para jogada que gere duas opções de marcar ponto, considerando as duas proximas jogadas

    """
    def __init__(self, posicao_tab=0):
        self.posicao_tab = posicao_tab
        self.jogadas = []
        self.vazio = '_'
        self.jogador1 = False
        self.ia = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                   (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        self.valor1 = "X"
        self.valor2 = "O"
        self.historico_jogador1 = ['jogador1']
        self.historico_jogador2 = ['jogador2']

    def tabuleiro(self):
        self.jogadas = []
        for i in range(9):
            self.jogadas.append(self.vazio)

    def imprimir_jogo(self):
        jogo = f'   {self.jogadas[0]} | {self.jogadas[1]} | {self.jogadas[2]}\n' \
               f'_______________\n' \
               f'   {self.jogadas[3]} | {self.jogadas[4]} | {self.jogadas[5]}\n' \
               f'_______________\n ' \
               f'  {self.jogadas[6]} | {self.jogadas[7]} | {self.jogadas[8]}'
        print(jogo)

class JogadorPc(AnalisarJogada):
    jogadas_livres = []
    def jogo_adversario_bloqueio(self):
        """buscar duas posições jogada pelo adversário com possibilidade de ganhar
        :return: retornar jogada que atende o requisito acima
        """
        self.jogadas_livres = []
        cont = 0
        for i in range(8):
            jog = [self.jogadas[self.ia[i][0]], self.jogadas[self.ia[i][1]],
                   self.jogadas[self.ia[i][2]]]
            if self.vazio in jog:
                for j in range(3):
                    if self.jogadas[self.ia[i][j]] == self.valor1:
                        cont += 1
                if cont > 1: # melhor chance do adversário
                    self.jogadas_livres = self.ia[i]
                    print(self.ia[i])
                    return True
                cont = 0
        return False
    def jogo_adversario_ofensiva(self):
        """Buscar duas posições com possibilidade de ganhar
        :return: retornar jogada que atende o requisito acima
        """
        cont = 0
        for i in range(8):
            jog = [self.jogadas[self.ia[i][0]], self.jogadas[self.ia[i][1]],
                   self.jogadas[self.ia[i][2]]]
            if not self.valor1 in jog:
                for j in range(3):
                    if self.jogadas[self.ia[i][j]] == self.valor2:
                        cont += 1
                if cont > 1:
                    # maior chance do adversário
                    self.jogadas_livres = self.ia[i]
                    print(self.ia[i])
                    return True
                else:
                    cont = 0
        return False
    def jogo_adversario_iniciativa(self):
        """jogar
        :return:        """
        self.jogadas_livres = []
        cont_vazio = 0
        cont_valor = 0

        jog0 = [0, 2, 4, 6, 8]
        if self.vazio in jog0:
            self.jogadas_livres = jog0
            return self.jogadas_livres

        for i in reversed(range(8)):
            jog1 = [self.jogadas[self.ia[i][0]], self.jogadas[self.ia[i][1]],
                    self.jogadas[self.ia[i][2]]]
            if not self.vazio in jog1:
                pass
            elif self.vazio in jog1:
                for j in range(3):
                    if self.jogadas[self.ia[i][j]] == self.vazio:
                        cont_vazio += 1
                    if self.jogadas[self.ia[i][j]] == self.valor2:
                        cont_valor += 1

                if cont_vazio > 0 and cont_valor > 0:
                    print(self.ia[i], 'seleção')
                    self.jogadas_livres =  self.ia[i]
                    return self.jogadas_livres

                elif cont_vazio > 0:
                    print(self.ia[i], 'seleção')
                    self.jogadas_livres =  self.ia[i]
                    return self.jogadas_livres
                cont_vazio = 0
                cont_valor = 0

        if len(self.jogadas_livres) < 3:
            self.jogadas_livres = self.ia[i]
        return self.jogadas_livres

    def posicao_de_jogada(self):
        """ 1- jogar na terceira posição com possibilidade de ganhar o jogo ou
            2- bloquear adversário, jogando na terceira posição com possilidade de ganhar ou
            3- jogar numa posição com possibilidade de formar 3 jogadas

            :return: retornar a posição que atender um dos requisitos acima observando a ordenação
        """
        posicoes_livres = []
        if self.jogo_adversario_ofensiva():
            jogo = self.jogadas_livres
        elif self.jogo_adversario_bloqueio():
            jogo = self.jogadas_livres
        else:
            jogo = self.jogo_adversario_iniciativa()
        for i in range(len(jogo)):
            if self.jogadas[jogo[i]] == self.vazio:
                posicoes_livres.append(jogo[i])
        return posicoes_livres

class Jogar(JogadorPc):
    vitoria_jogador1 = 0
    vitoria_jogador2 = 0
    empate = 0
    numeros_validos = (0, 1, 2, 3, 4, 5, 6, 7, 8)
    inicio = 1

    def iniciar_jogo(self):
        self.tabuleiro()
        self.jogador1 = False
        print("--" * 10)

        if int(self.inicio) == 3:
            pass
        elif int(self.inicio) == 1:
            self.jogada_pc_temp()

        while not self.jogo_terminou():
            val = input('Digite a posição desejada(1-9): ')
            try:
                if (int(val) -1) in self.numeros_validos:
                    self.posicao_tab = int(val) - 1
                    if self.inserir_jogada_temp():
                        self.jogada_pc_temp()
                else:
                    print('posição digitada excede o tamanho do tabuleiro')
            except:
                pass
        self.definir_placar()
    def select_jogador(self):
        if self.jogador1:
            self.jogador1 = False
        else:
            self.jogador1 = True

    def inserir_jogada_temp(self):
        if not self.jogo_terminou():
            if self.jogadas[self.posicao_tab] == self.vazio:
                valor = self.valor2 if self.jogador1 else self.valor1
                self.jogadas[self.posicao_tab] = valor
                if self.jogador1:
                    self.historico_jogador1.append(self.posicao_tab+1)
                else:
                    self.historico_jogador2.append(self.posicao_tab+1)
                self.select_jogador()
                return True
            else:
                print('posição já preenchida!')
        return False

    def jogada_pc_temp(self):
        try:
            pj = self.posicao_de_jogada()
            pc = random.choice(pj)
            self.posicao_tab = pc
            self.inserir_jogada_temp()
        except:
            print('erro na jogada_pc_temp')
    def jogador_vencedor(self):
        var = self.valor1
        for _ in range(2):
            ganhou = (
            self.jogadas[0] == var and self.jogadas[1] == var and self.jogadas[2] == var or
            self.jogadas[3] == var and self.jogadas[4] == var and self.jogadas[5] == var or
            self.jogadas[6] == var and self.jogadas[7] == var and self.jogadas[8] == var or

            self.jogadas[0] == var and self.jogadas[3] == var and self.jogadas[6] == var or
            self.jogadas[1] == var and self.jogadas[4] == var and self.jogadas[7] == var or
            self.jogadas[2] == var and self.jogadas[5] == var and self.jogadas[8] == var or

            self.jogadas[0] == var and self.jogadas[4] == var and self.jogadas[8] == var or
            self.jogadas[2] == var and self.jogadas[4] == var and self.jogadas[6] == var)
            if ganhou:
                return ganhou
            else:
                var = self.valor2
        return ganhou

    def jogo_terminou(self):
        self.imprimir_jogo()
        print("##"*10)
        if self.jogador_vencedor():
            return True
        elif not self.vazio in self.jogadas:
            return True
        return False

    def definir_placar(self):
        if self.jogador_vencedor():
            if self.jogador1:
                print('Jogador 1 venceu!')
                self.vitoria_jogador1 += 1
            else:
                print('jogador 1 venceu!')
                self.vitoria_jogador2 += 1

        elif not self.vazio in self.jogadas:
            print('Houve um empate!')
            self.empate += 1

        print('-'*8, 'Placar', '-'*11)
        print(f'Jogador(a)1: {aj.vitoria_jogador1}', '*' * aj.vitoria_jogador1)
        print(f'Jogador(a)2: {aj.vitoria_jogador2}', '*' * aj.vitoria_jogador2)
        print(f'Empates:     {aj.empate}', '*' * aj.empate)
        print('-'*8, 'Histórico','-'*8)
        print(self.historico_jogador1)
        print(self.historico_jogador2)

    def tt(self):
        cont = 0
        for i in range(8):
            jog = [self.jogadas[self.ia[i][0]], self.jogadas[self.ia[i][1]], self.jogadas[self.ia[i][2]]]
            if 0 in jog:
                for j in range(3):
                    if self.jogadas[self.ia[i][j]] == self.valor1:
                        cont += 1
                        print(self.jogadas[self.ia[i][j]])
            print(jog)




if __name__ == '__main__':
    aj = Jogar()
    continuar = 's'
    aj.inicio = '1'
    while continuar != 'n':
        if aj.inicio == '1' or aj.inicio == '2':
            print('1- Computador; 2- jogador; 3- Não perguntar')
            aj.inicio = input('Quem começa? (1 ou 2): ')
        aj.iniciar_jogo()
        continuar = input('Jogar novamente?(s/n): ')


