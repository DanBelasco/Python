def leiaint(a):

 while True:   
    leia = input(a)

    if leia.isnumeric():
        correto = int(leia)
        return correto        
        break
    else:
        print(f'  \n\n\033[31mErro. Digite um numero válido.\033[m')






#######################

correto = leiaint('\n\n Digite um numero inteiro: >>> ')

print(f'\n\nVocê digitou o numero >{correto}<')

print('\n')
print(f'\033[41m{" Programa encerrado ":^90}\033[m')
