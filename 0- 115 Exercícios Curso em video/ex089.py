from pprint import pprint

res2 = 0
lista = []
v1 = 0
v2 = 0
n = 0
print('\n\n')
print(f'Cadastro de alunos')
print('\n')

while True:
    nome = str(input('Nome:  >>> ')).capitalize()
    notaA = float(input('1º nota:  >>> '))
    notaB = float(input('2º nota:  >>> '))
    media = notaA + notaB / 2
    lista.append([nome,[notaA, notaB], media])
    print('\n-=-=-= Aluno Cadastrado com sucesso -=-=-=')
    res = ' '
    while res not in "SN":
        res = str(input('\nDeseja continuar? [S/N] >>> ')).strip().upper()[0]
    if res == 'N':
        break
print('\n\n\n')
print('-='*30)
print('nº Nome                                Média')
print('-'*60)
for n, nota in enumerate(lista):
    print(f'{n}  {lista[n][0]: <8}                        ', end='')
    print(f'{lista[n][2]:>7.1f}')
    
print('-'*60)
print('\n\n')

while True:
    res2 = int(input('\nQual aluno deseja mostrar as notas?\n [999] para interromper  >>> '))
    if res2 == 999:
        break
    print(f'\nAs notas do aluno nº{res2}  {lista[res2][0]} são: {lista[res2][1]}')
    
    

print('\n\n')
print(f'\033[41m{" Programa encerrado ":^90}\033[m')
print('\n\n')