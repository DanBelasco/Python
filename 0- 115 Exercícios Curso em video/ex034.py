
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


n1 = float(input('Digite o valor do salário: \n >>> '))

if n1 > 1250:
    n2 = n1 + n1 * 0.10
    print(f'\nSeu salário com o aumento de 10% fica no valor de: R${n2:.2f} \n')

else:
    n2 = n1 + n1 *0.15
    print(f'\nSeu salário com o aumento de 15% fica no valor de: R${n2:.2f}\n')


sleep(0.9)
print(f'\n\n{"":=^90}')
sleep(0.05)
print(f'{" Programa encerrado ":^90}')
sleep(0.05)
print(f'{"":=^90}\n\n\n')
