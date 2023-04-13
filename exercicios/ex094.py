



cadastroGeral = []
cadUnico = {}
totIdade = 0
medIdade = 0
mulheres = []
velhos = []
flag = 0
flag2 =0
print('\n')

while True:
    print('')
    cadUnico["nome"] = str(input('Nome:  >>>  ')).capitalize()

    sex =' '
    while sex not in "MF":
        sex = str(input('Sexo:  >>> ')).strip().capitalize()[0]

    cadUnico["sexo"] = sex
    cadUnico["idade"] = int(input('Idade:  >>>  '))
    totIdade = totIdade + cadUnico['idade']
    if cadUnico['sexo'] == "F":
        mulheres.append(cadUnico['nome'])

    cadastroGeral.append(cadUnico.copy())
    
    
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('\nDeseja continuar?\n \033[33m[S/N] >>>\033[m  ')).strip().capitalize()
    if continuar == 'N':
        break


print('\n')
#print(cadastroGeral)
print('=-'*30)
print(f'{"Resultado":^60}')
print('=-'*30)
media = totIdade/len(cadastroGeral)
print(f'\nNo total {len(cadastroGeral)} pessoas foram cadastradas')
print(f'A média de idade foi de {media:.2f}')
for c in cadastroGeral:
    for d ,q in c.items():
        if q == "F":
            flag = 1

  

if flag == 1:    
    print(f'As mulheres da lista são:' ,end=' ')
    for k in range(0,len(mulheres)):
        print(f'{mulheres[k]}', end=' ')
    print('')

else:
    print(f'Não foram cadastradas mulheres nesta lista')


for i in cadastroGeral:
    for p , l in i.items():
        if p == "idade" and l >= media:
            flag2 = 1

if flag2 == 1:
    print("\nLista de pessoas acima ou na média de idade")
    for i in cadastroGeral:
        for p, l in i.items():
            if p == "idade" and l >= media:
                print(f' => Nome: {i["nome"]}, Sexo: {i["sexo"]}, Idade: {i["idade"]}')



print('\n\n')
print(f'\033[41m{" Programa encerrado ":^90}\033[m')
print('\n\n')