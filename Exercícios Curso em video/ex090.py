

lik = dict()
lista =[]

print('\n\n\n')

for t in range(0,3):
    nome = str(input(f'Nome: >>> '))
    med = float(input(f'Média: >>> '))
    situa = ' '
    if med >= 7:
        situa ='Aprovado'
    else: situa = 'Reprovado'

    lik = {"nome": nome, "media": med, "situação": situa}
    lista.append(lik.copy())

print(f'\n\n{lik}\n\n')

for v in lista:
    for r, j, in v.items():
        print(f'{r} é igual a {j} ' )
    print('\n')

print('\n\n')
print(f'\033[41m{" Programa encerrado ":^90}\033[m')
print('\n\n')