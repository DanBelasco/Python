# gerar 5 numeros aleatorios e guardar em uma tupla
# mostrar a listagem dos numeros gerados 
# mostrar o maior e o menor

from random import randint
from random import sample



lista = (randint(0,99),randint(0,99),randint(0,99),randint(0,99),randint(0,99),randint(0,99),randint(0,99),randint(0,99),randint(0,99),randint(0,99))
lista2 = tuple(sample(range(99),10))


print(f'\n\nLista de números aleatórios: {lista}\n\n')
print(f'\n\nLista de números aleatórios 2 pelo metodo "tuple/Sample"  : {lista2}\n\n')

c = 0 
for m in lista:
    if c == 0:
        maior = m
        menor = m
    if m > maior:
        maior = m
    if m < menor:
        menor = m
    c = c+1

print(f'\nO maior numero utilizando "if" foi o : {maior} e o menor foi o: {menor}')

naOrdem = sorted(lista)

print(f'\n\nAjustudato fica: \n{naOrdem}')
print(f'\n\nO maior por "sorted" foi o: {naOrdem[9]} e o menor foi o: {naOrdem[0]}')

print(f'\n\n\nUtilizando "Max" e "Min" fica {max(lista)} e {min(lista)}')