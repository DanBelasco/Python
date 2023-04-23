

from time import sleep

sleep(0.05)
print(f'\n\n\n{"":=^90}')
sleep(0.05)
print(f'\033[42m{" INICIALIZANDO ":^90}\033[m')
sleep(0.05)
print(f'{"":=^90}\n')
sleep(0.05)
print(f'\n\033[36m{" Programa para calcular IMC ":=^90}\033[m\n\n')
sleep(0.05)


peso = float(input('\nDigite o seu peso atual:  \n  >>> '))
altura = float(input('\nDigite sua altura:  \n   >>> '))

imc = peso / (altura**2)

sleep(0.5)
print(f'\nCalculando . . .')
sleep(0.5)

if   imc < 18.5:
    print(f'\nSeu IMC é de {imc:.1f}Kg/m² e você está a baixo do seu peso ideal. \033[43mProcure um nutricionista.\033[m')
elif imc > 18.5 and imc <= 25:
    print(f'\nSeu IMC é de {imc:.1f}Kg/m² e você está no seu peso ideal. \033[42mPARABÉNS!\033[m')

elif imc > 25   and imc <= 30:
    print(f'\nSeu IMC é de {imc:.1f}Kg/m² e você está com sobrepeso. \033[44mFique atento!\033[m')

elif imc > 30   and imc <= 40:
    print(f'\nSeu IMC é de {imc:.1f}Kg/m² e você está com obesidade. \033[43mProcure um médico!\033[m')

elif imc > 40:
    print(f'\nSeu IMC é de {imc:.1f}Kg/m² e você está com obesidade mórbida. \033[41mPROCURE AJUDA O MAIS BREVE POSSÍVEL!\033[m')

sleep(0.9)
print(f'\n\n')
sleep(0.05)
print(f'\033[41m{" Programa encerrado ":^90}\033[m')
sleep(0.05)
print(f'\n\n\n')
