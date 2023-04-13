

# ler cinco valores em uma lista 
# mostrar o maior e o menor e em qual posição ele apareceu . se repetir o valor mostrar mesmo assim as posiçoes
mai = 0 
men = 0
valores = []
for c in range(0,5):
    valores.append(int(input(f'\nDigite um valor para a {c+1}º posição  >>>')))
    if c == 0:
        men = mai = valores[c]

    if  valores[c] > mai:
        mai = valores[c]
        
    if  valores[c] < men:
        men = valores[c]
        

print(f'\n\nA lista com os valores fica assim: {valores}')
print(f'\n o maior é o {mai} e o ele apareceu nas posições: ', end=' ')
for indice, conteudo in enumerate(valores):
    if conteudo == mai:
        print(f'[{indice +1}]  ', end=' '  )
print('\n')

print(f'\n o Menor é o {men} e o ele apareceu nas posições: ', end=' ')
for indice, conteudo in enumerate(valores):
    if conteudo == men:
        print(f'[{indice +1}] ' ,end=' ')

print(f'\n\n')
