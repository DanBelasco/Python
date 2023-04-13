from itertools import count
print(f'\n\n\n{"":=^90}')
print(f'{" Icinializando ":^90}')
print(f'{"":=^90}\n')
print(f'\n{" Programa para nomes ":=^90}\n\n')


n1 = input('Digite o nome completo >>> ').strip()

print(f'\nSeu nome em MAIUSCULO fica: {n1.upper()}')
print(f'\nSeu nome todo em minusculo: {n1.lower()}')
dividido = n1.split()


espa = n1.count(' ')
print(f'\nO total de letras no seu nome é de: {len(n1)- espa}')

#print(f'\nSeu primeiro nome tem {len(dividido[0])} letras no total')

print(f'\nSeu primeiro nome tem {n1.find(" ")} letras no total')

print(f'\n\n{"":=^90}')
print(f'{" Programa encerrado ":^90}')
print(f'{"":=^90}\n\n\n')