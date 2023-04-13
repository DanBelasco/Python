print('\n\n')


geral = [[],[]]

for d in range(0,7):
    val = int(input(f'Digite o {d+1}º valor >>>  '))
    if val %2 == 0:
        geral[0].append(val)
    else:
        geral[1].append(val)
    d = d + 1

print()

print(f'Os valores pares da sua lista são: {sorted(geral[0])}')
print(f'\nJá os impares são: {sorted(geral[1])}')

print('\n\n\n')
