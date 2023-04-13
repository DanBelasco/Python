from time import sleep

sleep(0.05)
print(f'\n\n\n{"":=^90}')
sleep(0.05)
print(f'\033[7m{" INICIALIZANDO ":^90}\033[m')
sleep(0.05)
print(f'{"":=^90}\n')
sleep(0.05)
print(f'\n\033[36m{" Programa para converter base numérica ":=^90}\033[m\n\n')
sleep(0.05)


n1 = int(input('Digite um número inteiro: \n >>>'))

print("""\nSelecione para qual tipo de base numérica deseja converter

Digite [0] para converter para base binário
Digite [1] para converter para base hexadecimal
Digite [2] para converter para base octal
Digite [3] para sair do programa
""")

opçao = int(input('\n >>> '))

if opçao == 0:
    print(f'\nO número \033[32m{n1}\033[m convertido para base binário é: \033[34m{bin(n1)[2:]}\033[2m\n')

elif opçao == 1:
    print(f'\nO número \033[32m{n1}\033[m convertido para base Hexadecimal é: \033[34m{hex(n1)[2:]}\033[m\n')

elif opçao == 2:
    print(f'\nO número \033[32m{n1}\033[m convertido para base Octal é: \033[34m{oct(n1)[2:]}\033[m\n')

elif opçao == 3:
    print(f'\n\033[33mVocê escolheu sair. tenha um bom dia! =D\033[m\n')
    

sleep(0.9)
print(f'\n\n')
sleep(0.05)
print(f'\033[7m{" Programa encerrado ":^90}\033[m')
sleep(0.05)
print(f'\n\n\n')