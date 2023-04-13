

list = ('arroz', 14.51, 
'feijão', 22.31, 'tomate', 4.02,
 'mandioca', 7.48, 'farinhda de trigo',
  5.60, 'óleo', 9.27, 'file de frango', 7.85,
  'alface', 2.30, 'vinagre', 2.51, 'ovos', 18.09,
  'sal', 5.52, 'açucar', 7.44, 'manteiga', 10.20)
print('\n\n')
print('='*40)
print(f'{"Mercado do Rincão":^40}')
print('='*40)
for c in range(0, len(list)):
    if c % 2 == 0:
        print(f'{list[c]:.<30}', end='')
    else:
        print(f'R${list[c]:>6.2f}')
print('\n\n')