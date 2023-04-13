

list =('bocejar','sono','preguiça',
'vontadededormir','fome', 'saudadedaminhacama', 
'cafeeee','picodeenergia', 'cafee', 'agua',
'musica', 'fone','notebook', 'noite', 'frio')

print('\n\n')
print('='*50)

for c in range(0,len(list)):
    print(f'Na palavra \033[33m{list[c]}\033[m tem: ' , end='')
    if "a" in list[c]:
        print('\033[34mA\033[m', end=' ')
    if "e" in list[c]:
        print('\033[34mE\033[m', end=' ')
    if "i" in list[c]:
        print('\033[34mI\033[m', end=' ')
    if "o" in list[c]:
        print('\033[34mO\033[m', end=' ')
    if "u" in list[c]:
        print('\033[34mU\033[m',end=' ')
    print('')
    
print('='*50)
print('\n\n')
print('='*50)
print(f'{"METODO GUANABARA":^45}')
print('='*50)


for c in list:
    print(f'\nna palavra \033[33m{c}\033[m temos ', end='')
    for letra  in c:
        if letra in "aeiou":
            print(f'\033[32m{letra.upper()}\033[m',end=' ' )