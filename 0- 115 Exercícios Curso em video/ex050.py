
acu1 = 0

for c in range(1,7):
    nu = int(input('Digite um numero inteiro \n  >>>'))
    if nu % 2 == 0:
        acu1 = acu1 + nu
        print("\nEsse era \033[42mPar\033[m e vai ser somado")

    else: print('\nEsse era \033[41mimpar.\033[m')

print(f'\nO valor total dos números pares é {acu1} ')
