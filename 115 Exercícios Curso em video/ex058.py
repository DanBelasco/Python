

# jogo da adivinhação.  criar um game que a maquina pense em um numero de 0 a 10 e eu tente adivinhar.
# Quando eu acertar o codigo deve dizer quantas tentativas foram nescessarias para eu aceertar.

import random

numaq = random.randint(0, 10)

print('\n\n\n pensei em um número de 0 até 10... \nVou te dar \033[43m5\033[m chances de acertar')
escolha = int(input('\nQual você acha que é ?? \n \033[33m>>>\033[m '))
tantas = 1 


while escolha != numaq:
    if tantas == 5 :
        print('Você usou as suas 5 chances e \033[41mPERDEU\033[m kkkkkkkkkkk\n\n\n')
        exit()
    escolha = int(input('NÃO, tente outra vez! \033[33m>>>\033[m '))
    tantas = tantas + 1
    


print(f'\n\n \033[42mACERTOU!\033[m e precisou chutar \033[33m{tantas}\033[m vezes para ganhar \n')

if  tantas == 1:
    print('\nMeus parabéns de primeira não é para qualquer um!\n\n')
elif tantas == 2:
    print('\nOlha, da segunda foi bom em!\n\n')
elif tantas == 3:
    print('\nFoi sorte..\n\n')
elif tantas == 4:
    print('\nJá estava quase perdendo rsrs\n\n')
elif tantas == 5:
    print('\nMas que sorte acertou na ultima chance hahaha\n\n')
