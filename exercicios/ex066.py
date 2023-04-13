maior = menor = soma = cont = 0

while True:
    n = int(input('Digite qualquer número e 999 para parar   >>>  '))
    if n == 999:
        break
    soma = soma + n
    cont = cont + 1
    if cont == 1:
        maior = n 
        menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
    

print(f'\n\nVocê Digitou {cont} números, e a soma deles no total foi de {soma}')
print(f'O maior número digitado foi o {maior} e o menor foi o {menor}\n\n')