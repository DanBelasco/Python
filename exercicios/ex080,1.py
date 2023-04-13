lista = []

for contador in range (0,5):
    numero = int(input('Digite um numero  >>> '))
    if contador == 0:
        lista.append(numero)
        print(f'\nO numero {numero} foi Adicionado ao final da lista')
    elif numero > lista[-1]:
        lista.append(numero)        
        print(f'\nO numero {numero} foi Adicionado ao final da lista')
    else:
        tamanho = 0
        while tamanho <= len(lista):
            if numero <= lista[tamanho]:
                lista.insert(tamanho,numero)
                print(f'\nO numero {numero} foi inserido na {tamanho}º posição. ')
                break
            tamanho = tamanho + 1

print(f'\n {lista}')


#cinco valores numericos 
#cadastrar em uma lista
#ja na posição correta da lista (sem sort())
# no final mostra a lista ordenda

#criar uma variavel para alocar o valor inserido no indice correto
    # deve-se comparar com os valores de dentro da lista para saber onde ele ira
    #se a lista estiver vazia ele sera o maior. logo íra como ultimo.
    # se for o menor ele ira para o primeiro 
    # e se for medio éra para o meio da lista?.