
from time import sleep

sleep(0.05)
print(f'\n\n\n{"":=^90}')
sleep(0.05)
print(f'{" Icinializando ":^90}')
sleep(0.05)
print(f'{"":=^90}\n')
sleep(0.05)
print(f'\n{" Programa para encontrar maior e menor ":=^90}\n\n')
sleep(0.05)



n1 = int(input('\ndigite o primeiro número \n  >>> '))
n2 = int(input('\ndigite o segundo número \n  >>> '))
n3 = int(input('\ndigite o terceiro número \n  >>> '))

#eliminando a possibilidade de numeros iguais
if n1 == n2 or n1 == n3 or n2 == n3:
    print('\033[41mDigite números diferentes uns dos outros\033[m')
    exit()

# encontrando o maior e menor com if
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

print(f'\nO maior número é o {maior} e o menor número é o {menor}')

#da para fazer colocando as veriaveis em uma lista e organizando tambem. mas eu nao lembro..

lista = [n1,n2,n3]
print(lista)


sleep(0.9)
print(f'\n\n{"":=^90}')
sleep(0.05)
print(f'{" Programa encerrado ":^90}')
sleep(0.05)
print(f'{"":=^90}\n\n\n')
