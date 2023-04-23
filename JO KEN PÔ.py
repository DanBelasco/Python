
Python

import random
from time import sleep
from unittest import result

sleep(0.05)
print(f'\n\n\n{"":=^90}')
sleep(0.05)
print(f'\033[42m{" INICIALIZANDO ":^90}\033[m')
sleep(0.05)
print(f'{"":=^90}\n')
sleep(0.05)
print(f'\n\033[36m{" Programa JoKenPô ":=^90}\033[m\n\n')
sleep(0.05)

print("""Ações:
Digite 0 para Pedra 
Digite 1 para Papel
Digite 2 para Tesoura\n""")

pessoa = int(input('Qual você escolhe??\n  >>> '))

lista =('pedra','papel', 'tesoura')

sleep(0.5)
print("JO")
sleep(0.5)
print("KEN")
sleep(0.5)
print('PÔ!\n')
sleep(0.5)

maquina = random.randint(0,2)


if pessoa == maquina:
    print(f'{ "=":=^30}')
    print(f'MÁQUINA JOGOU: {lista[maquina]}')
    print(f'JOGADOR JOGOU: {lista[pessoa]}')
    print(f'{"=":=^30}')
    print(f'\n       \033[43m{"EMPATE!"}\033[m       \n')

elif pessoa == 0 and maquina == 1:
    print(f'{ "=":=^30}')
    print(f'MÁQUINA JOGOU: {lista[maquina]}')
    print(f'JOGADOR JOGOU: {lista[pessoa]}')
    print(f'{"=":=^30}')
    print(f'\n\033[41m{"MÁQUINA VENCE!":^30}\033[m\n')

elif pessoa == 1 and maquina == 2:
    print(f'{ "=":=^30}')
    print(f'MÁQUINA JOGOU: {lista[maquina]}')
    print(f'JOGADOR JOGOU: {lista[pessoa]}')
    print(f'{"=":=^30}')
    print(f'\n\033[41m{"MÁQUINA VENCE!":^30}\033[m\n')

elif pessoa == 2 and maquina == 0:
    print(f'{ "=":=^30}')
    print(f'MÁQUINA JOGOU: {lista[maquina]}')
    print(f'JOGADOR JOGOU: {lista[pessoa]}')
    print(f'{"=":=^30}')
    print(f'\n\033[41m{"MÁQUINA VENCE!":^30}\033[m\n')

elif pessoa >2:
    print('\n\033[7mESCOLHA UM VALOR CORRETO!\033[m\n')

else:
    print(f'{ "=":=^30}')
    print(f'MÁQUINA JOGOU: {lista[maquina]}')
    print(f'JOGADOR JOGOU: {lista[pessoa]}')
    print(f'{"=":=^30}')
    print(f'\n\033[42m{"JOGADOR VENCE!":^30}\033[m\n')

sleep(0.9)
print(f'\n\n')
sleep(0.05)
print(f'\033[41m{" Programa encerrado ":^90}\033[m')
sleep(0.05)
print(f'\n\n\n')

