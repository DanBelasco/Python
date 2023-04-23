
from ntpath import join


pala = str(input('Digite uma frase que seja um palindromo  \n >>> ')).strip().upper()

lista = pala.split()
junto = ''.join(lista)
tamanho = len(junto)

inverso =''

for c in range(tamanho -1 , -1, -1):
    inverso = inverso + junto[c]


print(f'\nSua frase é: {junto}')
print(f'Sua frase invertida fica: {inverso}')

if inverso == junto:
    print(f'\nComo são iguais éssa frase é um PALINDROMO')
else:
    print('\nelas não são iguais')
