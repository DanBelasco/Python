
numeros = []

def line():
    print("=="*30) 


from random import randint
def sorteia():
    for c in range(0,5):
        numeros.append(randint(0,10))
    
    print('\n\n')
    line()
    print(f'   Os números sorteados foram: {numeros} ' )
    line()

def somaPar():
    ospares = 0
    for d in range(0, len(numeros)):
        if numeros[d] %2 == 0:
            ospares = ospares + numeros[d]


    print('')
    line()
    print(f'   A soma dos valores pares da lista acima é: {ospares}')
    line()
    
#--------------------------------
#      Programa principal

sorteia()
somaPar()

print('\n')
print(f'\033[41m{" Programa encerrado ":^90}\033[m')
