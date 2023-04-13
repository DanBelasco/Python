

from audioop import reverse
conta5 = 0 
contador = 0
lis = []

while True:
    valor = int(input(f'\nDigite um valor  >>>'))
    contador = contador + 1
    lis.append(valor)
    res = ' '
    while res not in 'SN':
        res = str(input('\n    Deseja continuar?   [S/N] \n  >>> ')).strip().upper()
    if res == 'N':
        break
print('\n\n\n')
print("-="*35)
print(f'\n\nForam digitados um total de {contador} numeros')
lis.sort(reverse= True)
print(f'\n{lis}')
if 5 in lis:
    print(f'\nSua lista contem o numero 5 e ele aparece nas posiões ' , end=' ')
    for posisão, conteudo in enumerate(lis):
        if conteudo == 5:
            conta5 = conta5 +1
            print(f'[{posisão + 1}]',end=' ')
else:
    print('\nSua lista não contém o numero 5!')
print(f'\nTotalizando {conta5} vezes na lista')
print('\n\n')
print('-='*35)
print('\n\n\n')