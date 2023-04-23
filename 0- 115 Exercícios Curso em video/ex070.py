#ler preço e nome dos produtos
# no final pergunta se quer continuar

#quanto foi gasto na compra
#quantos produtos custam mais de 300 reais
#qual o nome do produto mais barato
from time import sleep


print('\n\n------ Caixa aberto ------')
sleep(1)
cont = 0
total = 0
maisDe300 = 0
oMaisBarato = ' '
oMaisBaratovalor = 0

while True:
    print('\nPasse um produto')

    preco = float(input('\n  preço: >> '))
    
    total = total + preco

    nome = str(input('  nome: >> ')).strip().capitalize()

    if preco >= 300:
        maisDe300 = maisDe300 + 1
    
    if cont == 0:
        oMaisBarato = nome
        oMaisBaratovalor = preco
    
    if preco < oMaisBaratovalor:
        oMaisBaratovalor = preco
        oMaisBarato = nome
    
    cont = cont + 1
    
    parada = ' '
    while parada not in 'SN':
        parada = str(input('\nDeseja encerrar??  [S/N] \n >>>')).strip().upper()[0]

    if parada == 'S':
        break

print('encerrando...')
sleep(1.5)

print(f'\n>>>>>>> O total já com desconto a vista é de: R${total:.2f} <<<<<<<')
sleep(1)
if maisDe300 > 0 :
    print(f'\nEm sua compra existem {maisDe300} itens que custam mais de 300 reais.')
    print(f'isso te garante um total de {maisDe300 *3} Cupons da sorte no seu CPF!! ')
sleep(1)
print(f'\nO intem mais barado da sua compra foi: "{oMaisBarato}" que custou R${oMaisBaratovalor:.2f} \n\n')
