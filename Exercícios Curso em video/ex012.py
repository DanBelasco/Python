print(f'{"":=^90}')
print(f'{" Icinializando ":^90}')
print(f'{"":=^90}\n')
print(f'\n{" Programa calculador desconto de produtos ":=^90}\n\n')
        
n1 = float(input('Digite o valor do produto >>>'))

total = n1 - (n1 * 0.05)

print(f'\n\nO produto com desconto fica no valor de R${total:.2f} reais')

print(f'\n\n{"":=^90}')
print(f'{" Programa encerrado ":^90}')
print(f'{"":=^90}\n\n\n')