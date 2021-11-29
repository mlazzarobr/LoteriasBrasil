from lib.interface import *
from time import sleep

# Programa principal
while tipo != 8:
    tipo = menu(['Megasena', 'Quina', 'Lotomania', 'Lotofácil', 'Timemania', 'Dupla Sena', 'Personalizado', 'Sair do Programa'])

    if tipo == 7:
        a = int(input('Entre com o valor máximo do conjunto de valores: '))
        b = int(input('Entre com a quantidade de valores do conjunto: '))

    if tipo == 8:
        print()
        print('\033[32m-=\033[0;0m' * 5, end='')
        print(' \033[32m< BOA SORTE > \033[0;0m', end='')
        print('\033[32m-=\033[0;0m' * 5, end='\n')
        print()
        print('\033[31m** Programa encerrado **\033[0;0m \n')
        print()
        break

    qtjogos = int(input('Quantos jogos deseja? '))
    while i < qtjogos:
        if tipo == 1:
            randomize(60, 6)
        elif tipo == 2:
            randomize(80, 5)
        elif tipo == 3:
            print(f'Jogo {i+1}')
            randomize(100, 50)
            arrumaespelho = sorted(espelho)
            print('Aposta Espelho:')
            print(f'{arrumaespelho}')
            espelho.clear()
        elif tipo == 4:
            randomize(25, 15)
        elif tipo == 5:
            randomize(80, 10)
            tc = randint(0, 79)
            print(f'O time do coração é o {tc} - {listatimes[tc]}')
        elif tipo == 6:
            randomize(50, 6)
        elif tipo == 7:
            randomize(a, b)
        i += 1
    i = 0
