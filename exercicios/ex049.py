from time import sleep


sleep(0.05)
print(f'\n\n\n{"":=^90}')
sleep(0.05)
print(f'\033[42m{" INICIALIZANDO ":^90}\033[m')
sleep(0.05)
print(f'{"":=^90}\n')
sleep(0.05)
print(f'\n\033[36m{" Programa Taboada 2 ":=^90}\033[m\n\n')
sleep(0.05)

mult = int(input('Digite um numero inteiro \n\n  >>> '))

for c in range(0, 10):
    print(f'{mult} x {c} = {c * mult}')
    

sleep(0.9)
print(f'\n\n')
sleep(0.05)
print(f'\033[41m{" Programa encerrado ":^90}\033[m')
sleep(0.05)
print(f'\n\n\n')