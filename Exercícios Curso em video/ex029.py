print(f'\n\n\n{"":=^90}')
print(f'{" Icinializando ":^90}')
print(f'{"":=^90}\n')
print(f'\n{" Programa para policial rodoviário preguiçoso ":=^90}\n\n')



velo = int(input('Digite a velocidade do veículo \n >>> '))
multa =0
if velo > 80:
    print(f'\nO veículo foi multado pois estava á {velo}km/h em uma rodovia que o máximo é 80km/h\n')
    multa = (velo - 80) * 7 
    print(f'Sua multa será de R${multa + 100},00 \n\nA infração de velocidade é R$100,00 e para cada km/h a mais são R$ 7,00 de acrescimo\n')
 
else: print(f'\nVeículo dentro da velocidade permitida\n')

print(f'\n\n{"":=^90}')
print(f'{" Programa encerrado ":^90}')
print(f'{"":=^90}\n\n\n')
