resultado = {}
from random import randint
from operator import itemgetter

for c in range(0,8):
    resultado["jogador" + str(c+1)] = randint(1,6)



print('\n\n')
print('-=-=-= Ordem de jogada -=-=-=\n')
for d , f in resultado.items():
    print(f'{d} Tirou {f} nos dados')

print('\n\n')
print('-=-=-= Ordem do maior -=-=-=\n')

maior = dict(sorted(resultado.items(), key= itemgetter(1), reverse= True))

for q , w in maior.items():
    print(f'{q} Tirou {w} nos dados ')



print('\n\n')
print(f'\033[41m{" Programa encerrado ":^90}\033[m')
print('\n\n')