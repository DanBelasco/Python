from random import randint
from time import sleep

jogos1 = {}
c = 1

for cont in range(1, 5):
    jogada = randint(1, 6)
    jogos1["jogador" + str(cont)] = jogada
print('Valores sorteados:')
for k, v in jogos1.items():
    print(f'{k} tirou {v} no dado')
    
print('-=' * 30)
print(f'{"== RANKING DOS JOGADORES ==":^30}')
jogos2 = dict(sorted(jogos1.items(), key=lambda item: item[1], reverse=True))
for k, v in jogos2.items():
    print(f'{c}o. lugar: {k} com {v}.')
    c +=1
    