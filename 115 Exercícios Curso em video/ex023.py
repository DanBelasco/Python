print(f'\n\n\n{"":=^90}')
print(f'{" Icinializando ":^90}')
print(f'{"":=^90}\n')
print(f'\n{" Programa dos números ":=^90}\n\n')


n1 = int(input('Digite um numero de 0 até 9999  \n\n>>>>'))

u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10

print('\nO seu número digitado contém: ')
print(f'\nMilhar : {m}')
print(f'Centena: {c}')
print(f'Dezena : {d}')
print(f'Unidade: {u}\n')

print(f'\n\n{"":=^90}')
print(f'{" Programa encerrado ":^90}')
print(f'{"":=^90}\n\n\n')