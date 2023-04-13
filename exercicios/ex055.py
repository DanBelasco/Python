
maior = 0
menor = 0
for c in range(1,6):
    peso = float(input(f'Digite o peso da {c}ª pessoa  >>> '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f'\nO maior peso foi o de {maior}Kg e o menor foi de {menor}Kg')