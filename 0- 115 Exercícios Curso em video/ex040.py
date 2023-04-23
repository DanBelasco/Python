
from time import sleep

sleep(0.05)
print(f'\n\n\n{"":=^90}')
sleep(0.05)
print(f'\033[42m{" INICIALIZANDO ":^90}\033[m')
sleep(0.05)
print(f'{"":=^90}\n')
sleep(0.05)
print(f'\n\033[36m{" Programa para média escolar ":=^90}\033[m\n\n')
sleep(0.05)


n1 = float(input('\nDigite a primeira nota  \n  >>>  '))

n2 = float(input('\nDigite a segunda nota   \n  >>>  '))

media = (n1 + n2) / 2

if media <= 5:
    print(f'\n\033[41mREPROVADO!\033[m \nO aluno teve média de {media} pontos')

elif media >= 5 and media <= 6.9:
    print(f'\n\033[43mRECUPERAÇÃO!\033[m \nO aluno teve média de {media} pontos')

elif media >= 7:
    print(f'\n\033[42mAPROVADO!\033[m \nO aluno teve média de {media} pontos ')

sleep(0.9)
print(f'\n\n')
sleep(0.05)
print(f'\033[41m{" Programa encerrado ":^90}\033[m')
sleep(0.05)
print(f'\n\n\n')

