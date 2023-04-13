print(f'{"":=^90}')
print(f'{" Icinializando ":^90}')
print(f'{"":=^90}\n')
print(f'\n{" Programa para converter real para inteiro ":=^90}\n\n')

from math import floor
from math import trunc


n1 = float(input('Digite um numero Real >>> '))
sem_0 = floor(n1)
sem_01 = trunc(n1)
print(f'\nO numero digitado em valor inteiro fica :\n')

print(f'({sem_0}) - Pelo metodo ".Floor"')

print(f'\n({sem_01}) - Pelo metodo ".trunc"')

print(f'\n({int(n1)}) - Pelo metodo "int()"')

print(f'\n\n{"":=^90}')
print(f'{" Programa encerrado ":^90}')
print(f'{"":=^90}\n\n\n')