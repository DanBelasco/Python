from time import sleep
print()
def maior(* qualquercoisa):

    mai = 0
    c = 0


    while c < len(qualquercoisa):
        if c == 0:
            mai = qualquercoisa[c]
        elif qualquercoisa[c] > mai:
            mai = qualquercoisa[c]
        c = c + 1

    print('\n\n')
    print('=-'*30)
    print(f'Total de numeros informados {len(qualquercoisa)} \n ')
    sleep(1)
    print('Numeros..')
    for d in range(0, len(qualquercoisa)):
        print(f'{qualquercoisa[d]} .', end='', flush=True)
        sleep(0.2)
    print('')

    sleep(0.2)
    print('')
    print('=-'*30)
    print(f'\033[33mO maior número informado foi o\033[m {mai}')
    sleep(2)
    

#-------------------------------------------------

maior(1,1,2,3,4,5,4,3,)
maior(9999,81,24,5,123,43234,5555,3,34323,434)
maior(1,2)
maior(1)
maior(0)











print('\n\n')
print(f'\033[41m{" Programa encerrado ":^90}\033[m')
