from random import randint

matriz = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
tamanho_matriz = 6
somapar = 0
somacoluna4 = 0 
maior_linha = 0
print('\n\n')
for linha in range(0,tamanho_matriz):
    for coluna in range(0,tamanho_matriz):
        matriz[linha][coluna] = randint(0,100)
        print(f'Digite uma valor para [{linha},{coluna}]  >>> {matriz[linha][coluna]} ')
print('-='*30)
print(f'\n{"A matriz será:":^40}\n')

for linha in range(0,tamanho_matriz):
    for coluna in range(0,tamanho_matriz):
        if matriz[linha][coluna] %2 == 0:
            somapar = somapar + matriz[linha][coluna]
        print(f'[{matriz[linha][coluna]:^4}]' ,end='')
    print('')
print('-='*30)

print(f'\nA soma de todos os numero pares é: {somapar}')

for linha in range(0,tamanho_matriz):
    somacoluna4 = somacoluna4 + matriz[linha][2]
print(f'\nA soma de todos os valores da 3ª coluna é de {somacoluna4}')

for coluna in range(0,tamanho_matriz):
    if coluna == 0:
        maior_linha = matriz[4][coluna]
    elif matriz[4][coluna] > maior_linha:
        maior_linha = matriz[4][coluna]

print(f'\nO maior valor da 5º linha é o numero {maior_linha}')


print('\n\n')
print(f'\033[41m{" Programa encerrado ":^90}\033[m')
print('\n\n')