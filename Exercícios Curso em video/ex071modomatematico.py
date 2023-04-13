# cliente digita o valor e o caixa informa qual e quantas cédulas vão sair do caixa


print(f'{"":=^90}')
print(f'{" Bem vindo ao banco TowerGate ":^90}')
print(f'{"":=^90}\n')
print(f'\n{" Digite a quantidade que deseja sacar  ":=^90}\n')



n1 = int(input(' \n  Valor >>>'))

if n1 >=9999:
    print('\n\nDigite um valor abaixo de 9999\n\n')
    exit()

u = (n1 // 1 % 10) * 1
d = (n1 // 10 % 10) * 1
c = (n1 // 100 % 10) * 5
m = (n1 // 1000 % 10) * 20

print(f'\nAs cédulas sairão na seguinte ordem e quantidade\n')
print(f'{m} notas de R$50')
print(f'{c}  notas de R$20')
print(f'{d}   notas de R$10')
print(f'{u}   notas de R$1')

print(f' \nTotalizando R${m*50 + c*20 + d*10 + u*1}')