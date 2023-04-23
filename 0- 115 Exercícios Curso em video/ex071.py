print('\n\n')
print('==.'*15)
print('      Bem vindo ao banco TowerGate     ')
print('==.'*15)


nota = 50
totalDeNotas = 0

n = int(input('\n\nQaunto quer sacar?   >>> '))

montante = n

while True:
    if montante >= nota:
        montante = montante - nota
        totalDeNotas = totalDeNotas + 1
    else: 
        print(f'Sairão do caixa {totalDeNotas} notas de {nota}')
        if nota == 50:
            nota = 20
        elif nota == 20:
                nota = 10
        elif nota == 10:
                nota = 1
        totalDeNotas = 0
        if montante == 0:
            break
#    print(f'Sairão do caixa {totalDeNotas} notas de {nota}')
