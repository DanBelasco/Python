c = 0 
total = 0
soma = 0 

c = int(input('\nDigite algum numero ou \033[33m999\033[m para parar  >>>  '))

while c != 999:
    soma = soma + c
    total = total + 1
    c = int(input('\nDigite algum numero ou \033[33m999\033[m para parar  >>>  '))


print(f'\ncódigo parado\n ')
print(f'No total foram somados {total} numeros. E a soma deles é: {soma}\n\n\n')
