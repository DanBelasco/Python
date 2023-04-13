print(f'{"":=^90}')
print(f'{" Icinializando ":^90}')
print(f'{"":=^90}\n')
print(f'\n{" Programa calculador de tinta para parede ":=^90}\n')
        
alt = float(input("\nDigite a altura da parede em metros >>>  "))
larg = float(input('\nAgora digite a largura da parede em metros >>>'))

area = alt * larg

lts = area / 2

print(f'\nPara pintar essa parede de {area:.2f} m² voçê vai precisar de {lts:.2f} litros de tinta')

print(f'\n\n{"":=^90}')
print(f'{" Programa encerrado ":^90}')
print(f'{"":=^90}\n\n\n')