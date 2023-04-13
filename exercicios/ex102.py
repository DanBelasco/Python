def fac(a, show=False):
    '''
    *Função fatorial*

    Através do número informado, permite calcular o fatorial do mesmo.

    parametro  "a"   (obrigatório) =  Numero que será obtido o fatorial.
    parametro "show" (opicional)   =  quando True permite a exibição do processo do fatorial

    '''
    multi = 1
    if show == False:
        
        if a <= 0:
            print('Digite um valor maior que zero ')
        else:
            while a != 1:
                multi = multi * a
                a = a - 1
            return print(f'\n\n {multi}')
    
    else:
        print(f'\n {a}! é: {a}', end="")

        while a != 1 :
            multi = multi * a
            a  = a - 1 
            print(f'x{a}', end="")
    
        print(f' = {multi}\n\n')



###################################

fac(5)
print('\n')
print(f'\033[41m{" Programa encerrado ":^90}\033[m')


