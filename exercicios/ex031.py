print(f'\n\n\n{"":=^90}')
print(f'{" Icinializando ":^90}')
print(f'{"":=^90}\n')
print(f'\n{" Programa calculador de passagem ":=^90}\n\n')




n1 = float(input('\nQuantos kilometros serão a sua viagem? \n >>> '))


if n1 <= 200:
   totalmenos = n1 * 0.50
   print(f'\nSua viagem é de menos de 200km então vc paga R$0,50 centavos por km')
   print(f'\nPortanto sua passagem sairá pelo preço de R${totalmenos:.2f}')

if n1 >200:
    totalmais = n1 * 0.45
    print(f'\nSua viagem é de mais de 200km e por isso você só paga R$0,45 centavos por km')
    print(f'\nPortanto sua passagem sairá pelo preço de R${totalmais:.2f} ')


print(f'\n\n{"":=^90}')
print(f'{" Programa encerrado ":^90}')
print(f'{"":=^90}\n\n\n')
