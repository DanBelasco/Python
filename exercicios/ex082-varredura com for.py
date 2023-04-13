
par = []
impar = []
mmo = []
print('\n\n\n')
while True:
    numero = int(input('\nDigite um valor \n  >>> '))
    mmo.append(numero)
    res = ' '
    while res not in "SN":
        res = str(input(' \nDeseja continuar?? \n   [S/N] >>> ')).strip().upper()
    if res == 'N':
        break

print(f'\n\nAlista com os numeros ficam assim: {mmo}\n\n')

for posição, conteudo in enumerate(mmo):
    if conteudo %2 == 0:
        par.append(conteudo)
    else:
        impar.append(conteudo)

print(f'\nos pares são: {par}')
print(f'\nos imapres são: {impar}\n\n\n')    

