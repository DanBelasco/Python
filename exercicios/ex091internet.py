print('\n\n')

dic = dict()
q = 1
z=1
from audioop import reverse
from random import randint

for c in range(0,4):
    dic["jogador"+str(c+1)] = randint(1,6) 


print(f'-='*30)
print(f'{"Ordem dos dados":^60}')
print(f'-='*30)

for k, v in dic.items():
    print(f'{k} tirou {v} no dado')

print('')

dic2 = dict(sorted(dic.items(), key= lambda item: item[1]))

print(f'-='*30)
print(f'{"Menor valor":^60}')
print(f'-='*30)

for k, v in dic2.items():
    print(f'{z}º lugar {k} tirou {v} no dado')
    z = z + 1

print('')
print(f'-='*30)
print(f'{"Maior valor":^60}')
print(f'-='*30)

dic3 = dict(sorted(dic2.items(), key=lambda item: item[1], reverse = True))

for k, v,  in dic3.items():
    print(f'{q}º lugar {k} tirou {v} no dado')
    q = q + 1



print('\n\n')
print(f'\033[41m{" Programa encerrado ":^90}\033[m')
print('\n\n')