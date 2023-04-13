
fato = 1

numero = int(input('\n\nDigite um numero para saber o seu fatorial \n >>> '))
if numero <= 0:
    print(f'\n\n Escolha um numero positivo maior que zero ')
else:
    print(f'\n {numero}! é: {numero}', end="")

    while  numero != 1 :
        fato = fato * numero
        numero  = numero - 1 
        print(f'x{numero}', end="")
        
        
    print(f' = {fato}\n\n')