
from modulosss.matematica.moeda import*

from modulosss.uteis.encerra import cabô

print('\n\n')

valor = float(input('Digite o valor do produto: >>> '))


print(f'O dobro do valor do produto é: {dobro(valor)} ')



print(f'A metade do valor do produto é: {metade(valor)} ')
print(f'Com aumento de 10% temos: {aumento(valor,10)}')

print(f'Com o desconto de 15% fica: {diminui(valor,15)}')




cabô()