from time import sleep

sleep(0.05)
print(f'\n\n\n{"":=^90}')
sleep(0.05)
print(f'\033[7m{" INICIALIZANDO ":^90}\033[m')
sleep(0.05)
print(f'{"":=^90}\n')
sleep(0.05)
print(f'\n\033[36m{" Programa saber se o ano é bissexto ":=^90}\033[m\n\n')
sleep(0.05)


import datetime
ano = int(input('Digite o ano que quer analizar. ou "0" para ano atual \n >>> '))

if ano == 0:
    ano = datetime.date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'\n\033[41mO ano {ano} é bissexto\033[m\n')

else:
    print(f'\n\033[34mO ano\033[m \033[44m {ano} \033[m \033[34mNÃO é bissexto\033[m\n')

sleep(0.9)
print(f'\n\n')
sleep(0.05)
print(f'\033[7m{" Programa encerrado ":^90}\033[m')
sleep(0.05)
print(f'\n\n\n')
