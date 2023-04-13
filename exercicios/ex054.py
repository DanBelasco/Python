

# contar a idade de 7 pessoas e dizer quantas ja atingiram a maioridade. considerando como 21 anos

import datetime




ano = datetime.date.today().year

acumu = 0
acumu2 = 0 
acumu3 = 1
for c in range(1,8):
    data = int(input(f'Digite o ano de nascimento da {acumu3}ª pessoa  \n  >>> '))
    acumu3 = acumu3 + 1
    if ano - data >= 22:
        acumu = acumu + 1
    else: 
        acumu2 = acumu2 + 1
print(f'Ao todo {acumu} pessoas já atimgiram a maioridade, e {acumu2} ainda não atimgiram.' )








