
mulhercommenos = 0 
homenmaisvelho = ''
idadedohomenmaisvelho = 0
idade = 0
nome =''
totalidade = 0

for c in range(1,5):
    print(f'\n----{c}ª pessoa ----- ')
    nome = str(input('Digite o nome:   >> ')).strip()
    idade = int(input(f'Digite a idade:  >>'))
    sexo = str(input(f' Digite o sexo [M] ou [F]')).strip().capitalize()
    totalidade = totalidade + idade 
    if c == 1 and sexo == 'M':
        homenmaisvelho = nome
        idadedohomenmaisvelho = idade
    elif c == 1 and sexo == 'F' and idade < 20:
        mulhercommenos = 1
    else: 
        if sexo == 'M' and idade > idadedohomenmaisvelho:
            homenmaisvelho = nome
            idadedohomenmaisvelho = idade
        elif sexo == 'F' and idade < 20:
            mulhercommenos = mulhercommenos + 1

media = totalidade / c
print(f'\n\nA média de idades é de {media:.0f} anos')
if idadedohomenmaisvelho > 0:
    print(f'\nO homem mais velho é o {homenmaisvelho} e ele tem {idadedohomenmaisvelho} anos')
else:
    print(f'Nesse grupo não temos nenhum homem')

if mulhercommenos > 1:
    print(f'Nesse grupo temos {mulhercommenos} mulheres com menos de menos de 20 anos\n')
elif mulhercommenos == 1:
    print(f'Nesse grupo temos somente 1 mulher com menos de 20 anos \n')
elif mulhercommenos < 1 :
    print(f'Nesse grupo não temos nenhuma mulher com menos de 20 anos \n')
