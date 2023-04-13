
from modulosss.matematica.moeda import*

from modulosss.uteis.encerra import cabô

from modulosss.uteis.moeda_brasil import real


########################################################
print('\n\n')


valor = float(input('Digite o valor do produto: >>> '))




print(f'\nO dobro do valor do produto é: {real(dobro(valor))} ')
print(f'A metade do valor do produto é: {real(metade(valor))} ')
print(f'Com aumento de 10% temos: {real(aumento(valor,10))}')

print(f'Com o desconto de 15% fica: {real(diminui(valor,15))}')




cabô()