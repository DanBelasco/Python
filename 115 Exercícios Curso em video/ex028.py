print(f'\n\n\n{"":=^90}')
print(f'{" Icinializando ":^90}')
print(f'{"":=^90}\n')
print(f'\n{" Programa jogo da adivinhação ":=^90}\n\n')


from random import randint

n1 = randint(1,6)

user = int(input('Digite um número de 1 a 6 \n >>> '))

if user == n1:
    print(f'\nParabéns você acertou! O numero era o {n1} mesmo! =D \n')
else: print(f'\nInfelizmente você não acertou o número  =/\n')

print(f'\n\n{"":=^90}')
print(f'{" Programa encerrado ":^90}')
print(f'{"":=^90}\n\n\n')

