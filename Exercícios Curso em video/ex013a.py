print(f'{"":=^90}')
print(f'{" Icinializando ":^90}')
print(f'{"":=^90}\n')
print(f'\n{" Programa calculador aumento de salário baseado na porcentagem ":=^90}\n\n')
        
n1 = float(input('Digite o valor do salário >>>'))

n2 = int(input('\nDigite a porcentagem do aumento >>>'))

total = n1 + (n1 * (n2/100))

print(f'\n\nO salário com aumento de {n2}% fica no valor de R${total:.2f} reais')

print(f'\n\n{"":=^90}')
print(f'{" Programa encerrado ":^90}')
print(f'{"":=^90}\n\n\n')