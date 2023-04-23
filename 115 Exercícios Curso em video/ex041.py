import datetime
from time import sleep

sleep(0.05)
print(f'\n\n\n{"":=^90}')
sleep(0.05)
print(f'\033[42m{" INICIALIZANDO ":^90}\033[m')
sleep(0.05)
print(f'{"":=^90}\n')
sleep(0.05)
print(f'\n\033[36m{" Programa para categoria de nataçao ":=^90}\033[m\n\n')
sleep(0.05)

 
nasc = int(input('Digite sua data de nascimento  \n  >>> '))

data = str(datetime.date.today())

ano =int(data[0:4])

idade = ano - nasc

if idade <=9:
    print(f'\nVocê tem {idade} anos e sua categoria é a MIRIM')

elif idade >9 and idade <= 14:
    print(f'\nVocê tem {idade} anos e sua categoria é a INFATIL')

elif idade >14 and idade <= 19:
    print(f'\nVocê tem {idade} anos e sua categoria é a JUNIOR')

elif idade >19 and idade <=24:
    print(f'\nVocê tem {idade} anos e sua categoria é a SENIOR')

elif idade >24 :
    print(f'\nVocê tem {idade} anos e sua categoria é a MASTER')


sleep(0.9)
print(f'\n\n')
sleep(0.05)
print(f'\033[41m{" Programa encerrado ":^90}\033[m')
sleep(0.05)
print(f'\n\n\n')

