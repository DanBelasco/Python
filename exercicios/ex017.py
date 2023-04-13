from math import hypot

n1 = float(input('Digite a medida do Cateto oposto >>>'))

n2 = float(input('\nAgora digite a medida do Cateto adjacente >>>'))

hipo = ((n1**2) + (n2**2))**(1/2)


print(f'\nA hipotenusa desse triangulo é {hipo} pelo metodo matemático\n')

hipo2 = hypot(n1,n2)

print(f'\nA hipotenusa desse triangulo é {hipo2} pelo metodo ".hypot"\n')
