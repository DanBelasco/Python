print(f'\n\n\n{"":=^90}')
print(f'{" Icinializando ":^90}')
print(f'{"":=^90}\n')
print(f'\n{" Programa Par ou Ímpar ":=^90}\n\n')



n1 = int(input('Digite um número inteiro \n >>> '))

resu = n1 % 2

if resu == 0:
    print('\n\nO número digitado é PAR!')

else:
    print('\n\nO númeo digitado é Ímpar!!')


print(f'\n\n{"":=^90}')
print(f'{" Programa encerrado ":^90}')
print(f'{"":=^90}\n\n\n')
