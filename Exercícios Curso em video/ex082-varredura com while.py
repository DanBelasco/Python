contapar = 0 
caontaimpar = 0
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

print(f'\n\nAlista com os numeros ficam assim: {mmo}')

tamanho = 0 

while tamanho < len(mmo):
    if mmo[tamanho] %2 == 0:
        par.append(mmo[tamanho])
        contapar = contapar +1
    else:
        impar.append(mmo[tamanho])
        caontaimpar = caontaimpar + 1
    tamanho = tamanho + 1
     
print(f'\nos pares são: {par}')
print(f'\nos imapres são: {impar}')

if contapar == caontaimpar:
    print(f'\nVocê tem a mesma quantidade de numeros pares e impares')
elif contapar > caontaimpar:
    print(f'\nOs numero pares são á maioria ')
else:
    print(f'\nOs numero IMPARES são á maioria ')

print('\n\n\n')