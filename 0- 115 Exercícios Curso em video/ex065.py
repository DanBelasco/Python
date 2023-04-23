maior = 0
menor = 0 
contador = 0 
soma = 0 
vali = 's'

while  vali != 'N':
    c = int(input('\n\nDigite algum valor  >>>'))
    contador = contador +1
    soma = soma + c
    vali = str(input('\n    Deseja continuar? >>> ')).strip().upper()
    if contador == 1:
        maior = c
        menor = c
    elif c > maior:
        maior = c
    elif c < menor:
        menor = c
     
media = soma / contador
print(f'\n\nA media dos numeros digitados foi: {media} ')
print(f'\nO maior número foi o {maior} e o menor número foi o {menor}')