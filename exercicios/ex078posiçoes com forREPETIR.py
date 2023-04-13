#ler 5 valorese add em uma lista
# mostrar o maior e o menor e as suas posiçoes na lista
idades = list()
maior = 0 
menor = 0

for v in range(0,9):
    idades.append(int(input('Digite uma valor: >>>')))
    if v == 0:
        menor = idades[v]
        maior = idades[v]

    if idades[v] > maior:
        maior = idades[v]
        

    if idades[v] < menor:
        menor = idades[v]
        

print(f'\n\n{idades}')
print(f'\no maior é o número {maior} e ele está na posições:  ', end=' ')
for indice , conteudo in enumerate(idades):
    if conteudo == maior:
        print(f'{indice+1}...', end='')
print('')

print(f'\no menor é o número {menor} e ele está na posições: ' ,end='')
for indice, conteudo in enumerate(idades):
    if conteudo == menor:
        print(f'{indice+1}...',end='')
print('\n\n')
