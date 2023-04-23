#calculadora simples que le 2 valores e com o menu escolhe a operação

from time import sleep

sleep(0.05)
print(f'\n\n\n{"":=^90}')
sleep(0.05)
print(f'{" INICIALIZANDO ":^90}')
sleep(0.05)
print(f'{"":=^90}\n')
sleep(0.05)
print(f'\n\033[36m{" Programa calculadora simples com interface ":=^90}\033[m\n\n')
sleep(0.05)


n1 = int(input('\nDigite o primeiro valor  \n >>> '))
n2 = int(input('\nDigite o segundo valor  \n >>> '))


escolha = 0
while escolha != 5:

    print('''\n
[1] para soma
[2] para multiplicar
[3] para saber qual o maior 
[4] para mudar os numeros 
[5] para sair do programa
''')
    escolha = int(input(' qual a sua escolha?  \n >>> '))
    if escolha == 1:
        print(f' \n\n\033[33mResposta >>>>\033[m  {n1} + {n2} = {n1+n2}' )

    elif escolha == 2:
        print(f' \n\n\033[33mResposta >>>>\033[m  {n1} x {n2} = {n1*n2}')
    
    elif escolha == 3:
        if n1 == n2:
            print(f'  \n\n\033[33mResposta >>>>\033[m Os números {n1} e {n2} são iguais')
        elif n1 > n2:
            print(f' \n\n\033[33mResposta >>>>\033[m  {n1} é maior que {n2}. ')
        else:
            print(f' \n\n\033[33mResposta >>>>\033[m  {n2} é maior que {n1}. ')
    elif escolha == 4:
        n1 = int(input('\nDigite outro número para o primeiro valor \n  >>> '))
        n2 = int(input('\nDigite outro número para o segundo valor \n >>> '))
        print('\n\033[32mMudando os valore...\033[m')
    elif escolha == 5:
        print('\n\n\033[32mSaindo do programa...\033[m')

        sleep(0.9)
        print(f'\n\n')
        sleep(0.05)
        print(f'\033[41m{" Programa encerrado ":^90}\033[m')
        sleep(0.05)
        print(f'\n\n\n')
        exit()

    elif escolha >5 or escolha <1:
        print('\n\n\033[41mDigite uma valor correto!\033[m\n\n')
        

    sleep(2)
    
