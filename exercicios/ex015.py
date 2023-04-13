print(f'{"":=^90}')
print(f'{" Icinializando ":^90}')
print(f'{"":=^90}\n')
print(f'\n{" Programa para aluguel de carros ":=^90}\n\n')
        

dias = int(input('\nInforme a quantidade de dias utilizados >>>'))
km = float(input('\ninforme a quantidade de Kilometros rodados >>>> '))

total = (dias * 60) + (km * 0.15)

print(f'\nO carro rodou {km}Km por {dias} dias e o valor total a pagar é R${total:.2f}')


print(f'\n\n{"":=^90}')
print(f'{" Programa encerrado ":^90}')
print(f'{"":=^90}\n\n\n')