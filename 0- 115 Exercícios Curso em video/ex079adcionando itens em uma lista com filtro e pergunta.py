#digitar valores infinitos,  perguntanto se o usuario quer continuar
#cadastrar em uma lista 
#caso o numero ja esteja na lista, nao cadastrar e informar ao usuario. caso possivel. informar que foi adicionado 
#no final mostrar os valore adicionados em ordem crescentes

valor =[]

while True:
    usuario = int(input('\nDigite um valor  >>> '))
    if usuario in valor:
        print(f'\n\033[31mO valor {usuario} já está foi digitado e e não será adicionado\033[m')
    else:
        valor.append(usuario)
        print(f'\n\033[33mValor adcionionado\033[m')
    resp = ' '
    while resp not in "SN":
        resp = str(input(f'\nDeseja continuar?  [S/N] \n >>>')).strip().upper()[0]
    if resp == "N":
        break
            

print(f'\n\n os valores adicionados foram \n \033[33m{sorted(valor)}\033[m')