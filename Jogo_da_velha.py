'''
Autor: Lucas Gabriel Santos
Data: 08/01/2025
Versão: 1.0 (atualizado)
'''

import random, time

jogador1_letra = ''
jogador2_letra = ''
jogada_jogador1 = ''
jogada_jogador2 = ''
ganhador = 'n'
rodadas = 0
fim = False

# variáveis para funcionamento e verificação:

jogo_da_velha = ['A1', 'A2', 'A3',
       'B1', 'B2', 'B3',
       'C1', 'C2', 'C3']
posições = ['A1', 'A2', 'A3',
       'B1', 'B2', 'B3',
       'C1', 'C2', 'C3']

# definindo funções:

def definir_jogada_jogador(jog):
    jog  =''
    while jog not in jogo_da_velha:
        if jogador == 1:
            jog = input(f'{input_jogador1}: ').upper()
        else:
            jog = input(f'{input_jogador2}: ').upper()
        if jog not in jogo_da_velha:
            incorreto()
    return jog

def definir_jogada_bot(b):
    b = ''
    while b not in jogo_da_velha:
        b = random.choice(posições)
    time.sleep(1.5)
    return b

def velha():
    print(f'''{jogo_da_velha[0]} | {jogo_da_velha[1]} | {jogo_da_velha[2]}
--------------
{jogo_da_velha[3]} | {jogo_da_velha[4]} | {jogo_da_velha[5]}
--------------
{jogo_da_velha[6]} | {jogo_da_velha[7]} | {jogo_da_velha[8]}''')

def incorreto():
    print('\033[1;31mJogada inválida!!!\033[m')

def jogar_novamente():
    sn = 'z'
    global jogo_da_velha
    if ganhador != 'n':
        while sn not in 'sn':
            sn = input('Quer jogar novamente?').lower()
        if sn == 's':
            print('''
NOVO JOGO
''')
            jogo_da_velha = posições
        elif sn == 'n':
            global fim
            fim = True
    # jogo_da_velha = jogo_da_velha

def verificação_vitoria(letra):
    ganhador = 'n'

# verificando as colunas

    for c, v in enumerate(jogo_da_velha):
        if c > 2:
            break
        if jogo_da_velha[c] == letra:
            if jogo_da_velha[c+3] == letra and jogo_da_velha[c+6] == letra:
                ganhador = letra

#verificação das linhas

    for c, v in enumerate(jogo_da_velha):
        if posições[c] in 'A1B1C1':
            if jogo_da_velha[c] == letra:
                if jogo_da_velha[c+1] == letra and jogo_da_velha[c+2] == letra:
                    ganhador = letra

#verificação das diagonais

        if posições[c] == 'B2' and jogo_da_velha[c] == letra:
            if jogo_da_velha[c - 4] == letra and jogo_da_velha[c + 4] == letra:
                ganhador = letra
            elif jogo_da_velha[c - 2] == letra and jogo_da_velha[c + 2] == letra:
                ganhador = letra

    if ganhador == letra:
        print()
        print(f'{ganhador} venceu!!!')
        return ganhador

    return 'n'

while fim == False:
    if jogo_da_velha == posições:
        rodadas = 0

# definindo preferências:

        bj = 'n'
        while bj not in 'bj' or bj == '':
            bj = input('Jogar contra bot ou contra jogador? ').lower()
        xo = 'n'
        while xo not in 'XO' or xo == '':
            xo = input('Deseja jogar com X ou O ? ').upper()
        if xo == 'X':
            jogador1_letra = '\033[1;34mX\033[m'
            jogador2_letra = '\033[1;31mO\033[m'
        else:
            jogador1_letra = '\033[1;31mO\033[m'
            jogador2_letra = '\033[1;34mX\033[m'
        if bj in 'b':
            input_jogador1 = 'Sua jogada'
        else:
            input_jogador1 = f'Jogada de {jogador1_letra}'
            input_jogador2 = f'Jogada de {jogador2_letra}'
        posições = ['A1', 'A2', 'A3',
               'B1', 'B2', 'B3',
               'C1', 'C2', 'C3']

        velha()

    rodadas += 1
    print('''
>>>>>>>>>><<<<<<<<<<
''')

# jogada do 1° jogador:

    jogador = 1
    jogada_jogador1 = definir_jogada_jogador(jogada_jogador1)
    posição_jogador1 = posições.index(jogada_jogador1)
    jogo_da_velha[posição_jogador1] = jogador1_letra
    print(posições)
    velha()
    ganhador = verificação_vitoria(jogador1_letra)
    jogar_novamente()

    if fim == True or rodadas == 9:
        break

    print('''
>>>>>>>>>><<<<<<<<<<
''')

# verificação de novo jogo:
    if jogo_da_velha != posições:

        # jogada do 2° jogador (ou do bot):

        if bj[0] in 'b':
            jogada_jogador2 = definir_jogada_bot(jogada_jogador2)
            posição_jogador2 = posições.index(jogada_jogador2)
        else:
            jogador = 2
            jogada_jogador2 = definir_jogada_jogador(jogada_jogador2)
            posição_jogador2 = posições.index(jogada_jogador2)

        jogo_da_velha[posição_jogador2] = jogador2_letra
        velha()
        ganhador = verificação_vitoria(jogador2_letra)
        jogar_novamente()