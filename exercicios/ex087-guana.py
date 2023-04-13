


matriz = [[0,0,0],[0,0,0],[0,0,0]]
par = 0
somColu2 = 0
maior = 0
print('\n')
print('-='*30)

for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}] >>> '))
        
print(f'\n\n ')
print(f'Sua matriz será:\n')
for linha in range(0,3):    
    for coluna in range(0,3):
        if matriz[linha][coluna] %2 == 0:
           par = par + matriz[linha][coluna]   #soma de todos os pares
           
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print('')

for linha in range(0,3):
    somColu2 = somColu2 + matriz[linha][2]

print(f'\nA soma de todos os valores pares é: {par}')
print(f'\nA soma dos valores da 3º coluna é: {somColu2}')
print(f'\nO maior numero da segunda linha é: {maior}')
print('\n\n')
print(f'\033[41m{" Programa encerrado ":^90}\033[m')
