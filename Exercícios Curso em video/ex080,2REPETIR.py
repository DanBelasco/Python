
listao = []
print('\n\n\n')
for c in range(0,15):
    numeroDoUsuario = int(input(f'Digite o {c+1}º valor para ser alocado na lsita  >>>  '))
    if c == 0:
        listao.append(numeroDoUsuario) # se for o primeiro ele adiciona no ultimo valor com o append
        print(f'\n\nO valor {numeroDoUsuario} foi adicionado no \033[34mfinal da lista\033[m ') 
    elif numeroDoUsuario > listao[-1]:
        listao.append(numeroDoUsuario) # se for maior que o ultimo valor da lista '[-1]' ele adiciona no final tbm 
        print(f'\n\nO valor {numeroDoUsuario} foi adicionado no \033[34mfinal da lista\033[m ')
    else:
        posição = 0
        while posição <= len(listao):
            if numeroDoUsuario <= listao[posição]:
                listao.insert(posição,numeroDoUsuario)
                print(f'\n\nO valor {numeroDoUsuario} foi inserido na \033[33m{posição}º posição\033[m ')
                break

            posição = posição + 1
        
print(f'\n\n{listao}')
    



#cinco valores numericos 
#cadastrar em uma lista
#ja na posição correta da lista (sem sort())
# no final mostra a lista ordenda

    #criar uma variavel para alocar o valor inserido no indice correto
    # deve-se comparar com os valores de dentro da lista para saber onde ele ira
    #se a lista estiver vazia ele sera o maior. logo íra como ultimo.
    # se for o menor ele ira para o primeiro 
    # e se for medio éra para o meio da lista?

     # verificador para saber se é o primeiro numero
  

    # verificador para saber se ele é maior que o ultimo 
    # número inserido
    #caso o numero seja menor que o ultimo e nao seja o 1º

    #o codigo faz um loop de varredura no tamanho da lista
    #Ele vai verificar dentro de cada posição se o numero que
    #eu quero inserir é menor ou igual a ele     
    #Como não precisa proceguir usa-se o break

    #acumulador para que a posição avance
