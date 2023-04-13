from time import sleep

def trace():
    print('')
    print('=-'*35)
    

def trace2():
    print('--'*35)
    

def contador(ini,fim,passo):
    print('\n\n')
    trace()


    trace2()


    
    print('\n')

   

    if passo < 0:
        posi = passo * (-1)
    else:
        posi = passo

    if posi == 0:
        posi = 1



    if ini > fim:

        while ini >= fim:
            print(f'{ini}. ', end='' , flush=True)
            ini = ini - posi
            sleep(0.1)
        print('')



    elif ini < fim:

        while ini <= fim:        
            print(f'{ini}. ', end='' , flush=True)
            ini = ini + posi
            sleep(0.1)
        print(f'{fim}. ')
        print('')








#--------------------------------

contador(10,5,1)
contador(0,250,7)

trace()
print(' Contagem com parametros  ')
trace2()
i = int(input('Inicio: >>> '))
f = int(input('Fim: >>> '))
p = int(input('Passo: >>> '))
print('')
trace2()

contador(i,f,p)


print('\n\n')
print(f'\033[41m{" Programa encerrado ":^90}\033[m')
print('\n\n')