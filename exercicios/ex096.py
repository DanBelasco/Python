def calc_area(comprimento, largura):
    area = comprimento * largura
    print(f'\n\nA area do lote informado tem o tamanho de {area}m²')

print(f'\nPrograma calculdor de area ')

comprimento = float(input('\nComprimento: >>>  '))
largura = float(input('Largura: >>> '))


calc_area(comprimento, largura)

print('\n\n')
print(f'\033[41m{" Programa encerrado ":^90}\033[m')
print('\n\n')
