
#par ou impar se eu perder o jogo acaba e mostra quantas
#  vezes eu ganhei do computador

from random import randint
from time import sleep
conta = 0

print('\n\nVamos jogar par ou impar para ver até quanto vc ganha?\n')
sleep(2)

while True:
    pessoa = int(input(f'\n\nescolhe e digite um numero inteiro   >>>>  '))
    parouimpar = str(input('\nVocê quer par ou impar??  [P/i]  ')).strip().capitalize()
    maquina = randint(0,10)
    print(f'\n ok eu escoho o {maquina}')
    sleep(2)
    total = pessoa + maquina
    print(f'\n humm {pessoa} + {maquina} é igual a : {total}')
    sleep(2)
    resupessoa = total % 2
    if resupessoa == 0 and parouimpar == 'P':
        print(f'\n\n\033[32mVocê ganhou\033[m {total} é par')
        conta = conta +1
    elif resupessoa == 0 and parouimpar == 'I':
        print(f'\n\n033[41mVocê perdeu\033[m {total} é par')
        break

    elif resupessoa != 0 and parouimpar == 'I':
        print(f'\n\n\033[32mVocê ganhou\033[m {total} é impar')
        conta = conta +1
    elif resupessoa != 0 and parouimpar == 'P':
        print(f'\n\n\033[41mVocê perdeu\033[m {total} é impar')
        break
print(f'\nNo total você ganhou \033[33m{conta}\033[m vezes!\n\n')        
