
total = 1
xouigual = 0
num = int(input('\n\nDigite o numero que deseja saber o fatorial  \n\n  >>> '))
print(f'\n\n {num}! é: ',end='')
for cont in range(num ,0,-1):
    if cont == 1:
        xouigual = ' ='
    else:
        xouigual = 'x'
    total = total * cont
    print(f'{cont}{xouigual}', end="")

print(f' {total}\n\n')