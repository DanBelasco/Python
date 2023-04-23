from time import sleep

sleep(0.05)
print(f'\n\n\n{"":=^90}')
sleep(0.05)
print(f'{" Icinializando ":^90}')
sleep(0.05)
print(f'{"":=^90}\n')
sleep(0.05)
print(f'\n{" Programa para calcular salário ":=^90}\n\n')
sleep(0.05)

n1 = int(input('Digite o tamanho da primeira reta \n >>> '))
n2 = int(input('\nDigite o tamanha da segunda reta \n >>> '))
n3 = int(input('\nDigite o tamanho da terceira reta \n >>> '))

if n1 < (n2 + n3) and n2 < (n1 + n3) and n3 < (n1 + n2):
    print(f'\nOs segmentos de reta {n1}, {n2} e {n3}. podem formar um triangulo')

else:
    print(f'\nOs segmentos de reta {n1}, {n2} e {n3} NÃO podem formar um triangulo')

sleep(0.9)
print(f'\n\n{"":=^90}')
sleep(0.05)
print(f'{" Programa encerrado ":^90}')
sleep(0.05)
print(f'{"":=^90}\n\n\n')
