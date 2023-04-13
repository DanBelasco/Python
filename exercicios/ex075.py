

#inserir 4 valores em uma tupla pelo usuario
#mostrar os valores da tupla
#quantos 9 tinham nos numeros
#em que posição foi digitado o primeiro valor 3
#quais foram os numeros pares


from itertools import count
totaldepar = 0


lista = ( int(input('\n\n\nDigite o primeiro valor  >>')), int(input('Digite o segundo valor  >>')),
int(input('Digite o terceiro valor  >>')), int(input('Digite o quarto valor  >>')))

print(f'\nVocê digitou os valores {lista}')
quantos9 = lista.count(9)
if 9 in lista:
    print(f'Na sua lista de numeros o 9 apareceu {quantos9} vezes')
else: 
    print(f'Não existe nenhum numero 9 na sua lista de numeros')

if 3 in lista:
    print(f'O primeiro numero 3 da sua lista é o {lista.index(3) +1}º numero digitado')
else:
    print(f'Não existe nenhum 3 na sua lista')


print('Os pares da lista são : ' , end='')

for c in lista:
    if c %2 == 0:
        print(f'{c}', end=' ' )
        totaldepar = totaldepar + 1
    
            
if totaldepar == 0:
    print(f'Não existem numeros pares na sua lista')
