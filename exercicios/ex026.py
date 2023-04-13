print(f'\n\n\n{"":=^90}')
print(f'{" Icinializando ":^90}')
print(f'{"":=^90}\n')
print(f'\n{" Programa para encontrar a letra >A< na frase ":=^90}\n\n')


from itertools import count


n1 = str(input('Digite uma frase  \n >>> ')).strip().lower()

total = n1.count("a")
print(f'\nNa sua frase existem {total} letras "a"')

posi = n1.find('a') + 1

print(f'\nA primeira letra "a" que aparece é a {posi}º letra\n')

ult = n1.rfind('a') + 1

print(f'A ultima letra "a" que aparece é a {ult}º ')

print(f'\n\n{"":=^90}')
print(f'{" Programa encerrado ":^90}')
print(f'{"":=^90}\n\n\n')

