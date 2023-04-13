print('\n')
pesanome = ''
pesado = 0
levnome =''
leve = 0
listao = []
galera =[]
contador = 0

while True:
    print(' ')
    galera.append(str(input('Digite o nome :  ')).capitalize())
    galera.append(int(input('Qual o peso ? :  ')))
    listao.append(galera[:])
    contador = contador + 1
    galera.clear()
    print('')

    res = ' '
    while res not in 'SN':
        res = str(input('\nContinue? [S/N] >>>  ')).strip().upper()[0]
    if res == 'N':
        break

print('\n')
print(f'Foram adicionadas {contador} pessoas nessa lista \n')
print(listao)
print('')
for p in range(0,len(listao)):
    if p == 0:
        pesado = listao[0][1]
        pesanome = listao[0][0]
        leve = listao[0][1]
        levnome = listao[0][0]

    elif listao[p][1] > pesado:
        pesado = listao[p][1]
        pesanome =listao[p][0]

    elif listao[p][1] < leve:
        leve = listao[p][1]
        levnome =listao[p][0]
    p = p + 1


print(f'o maior peso foi de {pesado}Kg. peso de ', end='' )

for d in range(0,len(listao)):
    if listao[d][1] == pesado:
        print(f'{listao[d][0]}' ,end='. ')
    d = d + 1
print('')

print(f'O menor peso foi de {leve}Kg. Peso de ' ,end='' )

for t in range(0,len(listao)):
    if listao[t][1] == leve:
        print(f'{listao[t][0]}' ,end='. ')
    t = t + 1

print('\n\n')