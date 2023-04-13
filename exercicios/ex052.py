
#se for divisivél mais de 2 vezes não é primo

nume = int(input('Digite um número inteiro   \n >>>> '))
total = 0
for c in range(1,nume + 1):
    if nume % c ==0:
        print('\033[34m', end=' ')
        total = total + 1
    else:
        print('\033[33m', end=' ')
    print(f'{c}', end=' ')
print('\033[m')

if total >2:
    print(f'\nesse numero foi divisivel por {total} vezes e por isso não é primo  =(' )
else:
    print(f'\nesse número foi divisivel por somente 2 vezes por isso é primo!!!')