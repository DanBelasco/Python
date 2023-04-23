

nome = str(input('\nDigite seu nome completo \n >>>')).strip().capitalize()

se = str(input('\nDigite seu sexo [M/F} \n >>>')).strip().upper()

while se not in ['F','M']:
    se = str(input('\nDigite o caractere correto!  \n >>>')).strip().upper()

ano = str(input(f'\n{nome}, digite seu ano de nascimento \n >>>'))

cpf = int(input('\nDigite seu cpf: \n >>>'))

print(f'\nO nome digitado foi o "{nome}". \n está correto? \n   ')

certoerrado =str(input('  \033[33m[S/N]\033[m >>>  ')).strip().upper()

if certoerrado == 'N':
    print('\n\033[41mfaça novamente o cadastro!\033[m')
    exit()



print(f'\nO sexo digitado foi o "{se}". \n está correto? \n   ')

certoerrado =str(input('  \033[33m[S/N]\033[m >>>  ')).strip().upper()

if certoerrado == 'N':
    print('\n\033[41mfaça novamente o cadastro!\033[m')
    exit()

print(f'\nO ano de nascimento digitado foi o "{ano}". \n está correto? \n   ')

certoerrado =str(input('  \033[33m[S/N]\033[m >>>  ')).strip().upper()

if certoerrado == 'N':
    print('\n\033[41mfaça novamente o cadastro!\033[m')
    exit()

print(f'\nO CPF digitado foi o "{cpf}". \n está correto? \n   ')

certoerrado =str(input('  \033[33m[S/N]\033[m >>>  ')).strip().upper()

if certoerrado == 'N':
    print('\n\033[41mfaça novamente o cadastro!\033[m')
    exit()


print('\n\n\033[32mObrigado! =D\033[m\n')

