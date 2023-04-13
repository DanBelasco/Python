print(f'\n\n\n{"":=^90}')
print(f'{" Icinializando ":^90}')
print(f'{"":=^90}\n')
print(f'\n{" Programa para escolher a order dos alunos ":=^90}\n\n')



from random import shuffle

n1 = input('1º nome: >>> ')
n2 = input('2º nome: >>> ')
n3 = input('3º nome: >>> ')
n4 = input('4º nome: >>> ')


lis = [n1,n2,n3,n4,]

dado = shuffle(lis)

print(f'\nA ordem da apresentação dos alunos será:\n')
print(lis)


print(f'\n\n{"":=^90}')
print(f'{" Programa encerrado ":^90}')
print(f'{"":=^90}\n\n\n')