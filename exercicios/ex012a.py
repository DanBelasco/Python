print(f'{"":=^90}')
print(f'{" Icinializando ":^90}')
print(f'{"":=^90}\n')
print(f'\n{" Programa calculador desconto de produtos ":=^90}\n\n')
        
n1 = float(input('Digite o valor do produto >>>'))

total = n1 - (n1 * 0.05)
prazo = n1 + (n1 * 0.08)


print(f'\n\nO produto pagando a vista tem um desconto de 15% e fica R${total:.2f} reais')
print(f'\n\nO produto pagando no cartão tem um acréscimo de 8% efica R${prazo:.2f} reais')


print(f'\n\n{"":=^90}')
print(f'{" Programa encerrado ":^90}')
print(f'{"":=^90}\n\n\n')