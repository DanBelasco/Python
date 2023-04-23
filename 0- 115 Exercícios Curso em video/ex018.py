print(f'{"":=^90}')
print(f'{" Icinializando ":^90}')
print(f'{"":=^90}\n')
print(f'\n{" Programa para trigonometria ":=^90}\n\n')

from math import sin,cos,tan,radians

ang1 = float(input('Digite o valor do angulo >>>'))

ang = radians(ang1)

sen = sin(ang)
cos = cos(ang)
tan = tan(ang)

print(f'\nO angulo {ang1} tem um Seno de {sen:.2f}')
print(f'\nO angulo {ang1} tem um Cosseno de {cos:.2f}')
print(f'\nO angulo {ang1} tem uma tangente de {tan:.2f} \n')

print(f'\n\n{"":=^90}')
print(f'{" Programa encerrado ":^90}')
print(f'{"":=^90}\n\n\n')