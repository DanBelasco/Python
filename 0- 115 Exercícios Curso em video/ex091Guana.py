print('\n\n')

dic = dict()
q = 1
z=1

from random import randint
from operator import itemgetter

for c in range(0,4):
    dic["jogador"+str(c+1)] = randint(1,6) 


print(f'-='*30)
print(f'{"Ordem dos dados":^60}')
print(f'-='*30)

for k, v in dic.items():
    print(f'{k} tirou {v} no dado')

print('')





dic2 = dict(sorted(dic.items(), key= itemgetter(1), reverse = True ))

print(f'-='*30)
print(f'{"Ordem do ganhador":^60}')
print(f'-='*30)

for k, v in dic2.items():
    print(f'{z}º lugar {k} tirou {v} no dado')
    z = z + 1


print('\n\n')
print(f'\033[41m{" Programa encerrado ":^90}\033[m')
print('\n\n')