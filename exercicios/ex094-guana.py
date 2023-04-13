
listaGeral = []
dicPessoa = {}
somaIdade = 0

while True:
    print('')
    dicPessoa["nome"]= str(input('Nome: >>> ')).strip().capitalize()
    dicPessoa["sexo"]= str(input('Sexo: >>> ')).strip().capitalize()[0]
    dicPessoa["idade"]= int(input('Idade: >>> '))
    somaIdade = somaIdade + dicPessoa['idade']

    listaGeral.append(dicPessoa.copy())

    res = ' '
    res = str(input('\nDeseja continuar??\n  [S/N]  >>>  ')).strip().capitalize()[0]
    if res == 'N':
        break

print('')
print(listaGeral)
print('=-'*30)

'''
print(f'\nNo total foram cadastradas {len(listaGeral)} pessoas') 

mediaIdades = somaIdade / len(listaGeral)

print(f'\nA média das idades é {mediaIdades:.2f}')

print(f'\nAs mulheres da lista são: ' ,end='')
for c in listaGeral:
    if c["sexo"] == 'F':
        print(f'{c["nome"]}.', end=' ')
print('')

print(f'\nLista das pessoas que estão acima da média: ' ,end='')
for m in listaGeral:
    if m["idade"] >= mediaIdades:
        print(f' => Nome: {m["nome"]} tem {m["idade"]} anos')
    print('')

'''