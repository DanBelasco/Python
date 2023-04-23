

from time import sleep

sleep(0.05)
print(f'\n\n\n{"":=^90}')
sleep(0.05)
print(f'\033[42m{" INICIALIZANDO ":^90}\033[m')
sleep(0.05)
print(f'{"":=^90}\n')
sleep(0.05)
print(f'\n\033[36m{" Programa para alistamente militar ":=^90}\033[m\n\n')
sleep(0.05)

import datetime


nasc = int(input('Digite o ano de nascimento \n  >>>  '))

atual = str(datetime.date.today())


ano = int(atual[0:4])
mes = (atual[5:7])

idade = (ano - nasc)

if idade == 17:
    print(f'\n\nVocê já tem idade para se alistar voluntariamente. Mas ano que vem você deve ir ao alistamento obrigatoriamente')

elif idade < 17:
    print(f'\n\nVocê ainda não tem idade suficiente para o alistamento militar volte em {17 - idade} anos.') 

elif idade == 18:
    print(f'\n\nVocê deve se apresentar em uma junta militar de janeiro de {ano} até junho de {ano}')

elif idade > 18:
    print(f'\n\nVocê já passou do alistamento {idade - 18} anos. Compareça em uma junta para regularizar sua situação')



sleep(0.9)
print(f'\n\n')
sleep(0.05)
print(f'\033[41m{" Programa encerrado ":^90}\033[m')
sleep(0.05)
print(f'\n\n\n')

