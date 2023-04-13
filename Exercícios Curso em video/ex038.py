
from time import sleep

sleep(0.05)
print(f'\n\n\n{"":=^90}')
sleep(0.05)
print(f'\033[7m{" INICIALIZANDO ":^90}\033[m')
sleep(0.05)
print(f'{"":=^90}\n')
sleep(0.05)
print(f'\n\033[36m{" Programa para encontrar o maior número ":=^90}\033[m\n\n')
sleep(0.05)



n1 = int(input('\nDigite o primeiro número  \n \033[34m>>>\033[m '))
n2 = int(input('\nDigite o segundo número  \n \033[34m>>>\033[m  '))

if n1 == n2:
    print(f'\n\033[43mNão existe valor maior!\033[m  {n1} e {n2} são iguais.')

elif n1 > n2 :
    print(f'\nO número \033[42m{n1}\033[m é maior que \033[41m{n2}\033[m!')

elif n2 > n1 :
    print(f'\nO número \033[42m{n2}\033[m é maior que o núnermo \033[41m{n1}\033[m!')


sleep(0.9)
print(f'\n\n')
sleep(0.05)
print(f'\033[7m{" Programa encerrado ":^90}\033[m')
sleep(0.05)
print(f'\n\n\n')

