from random import randint
pc = 0
com =0 
jogo = []
print('\n\n\n')
total = int(input('Quantos jogos você gostaria?  \n >>> '))

for c in range(0,total):
    for j in range(0,6):
        while pc in jogo:
            pc = randint(0,60)
        if pc not in jogo:
            jogo.append(pc)
        

    print(f'{sorted(jogo)}')
    print('')
    jogo.clear()



print('\n\n')
print(f'\033[41m{" Programa encerrado ":^90}\033[m')
print('\n\n')