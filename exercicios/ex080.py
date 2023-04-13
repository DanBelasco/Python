

#cinco valores numericos 
#cadastrar em uma lista
#ja na posição correta da lista (sem sort())
# no final mostra a lista ordenda

#criar uma variavel para alocar o valor inserido no indice correto
    # deve-se comparar com os valores de dentro da lista para saber onde ele ira
    #se a lista estiver vazia ele sera o maior. logo íra como ultimo.
    # se for o menor ele ira para o primeiro 
    # e se for medio éra para o meio da lista?

print('\n\n')
listnum = []


for contador in range(0,50):
    numero = int(input('\ndigite um numero  >>  '))
    
    if  contador == 0:                              # verificador para saber se é o primeiro numero
        listnum.append(numero)  
        print(f'\nAdicionado ao final da lista')
    elif numero > listnum[-1]:                        # verificador para saber se ele é maior que o ultimo 
        listnum.append(numero)                      # número inserido
        print(f'\nAdicionado ao final da lista')

    else:                                          #caso o numero seja menor que o ultimo e nao seja o 1º
        posição = 0
        while posição < len(listnum):              #o codigo faz um loop de varredura no tamanho da lista
            if numero <= listnum[posição]:          #Ele vai verificar dentro de cada posição se o numero que
                listnum.insert(posição,numero)      #eu quero inserir é menor ou igual a ele
                print(f'O numero {numero} foi adicionado na posição {posição} da lista')
                break                               #Como não precisa proceguir usa-se o break

            posição = posição + 1                   #acumulador para que a posição avance

print(f'\n{listnum}')
print('\n\n')
