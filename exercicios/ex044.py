from time import sleep

sleep(0.05)
print(f'\n\n\n{"":=^90}')
sleep(0.05)
print(f'\033[42m{" INICIALIZANDO ":^90}\033[m')
sleep(0.05)
print(f'{"":=^90}\n')
sleep(0.05)
print(f'\n\033[36m{" Programa para calcular descontos ":=^90}\033[m\n\n')
sleep(0.05)

preco = float(input('\nDigite o valor do produto: \n  >>> '))

print(f'''\nSelecione o método de pagamento

[0]>> À vista no dinheiro ou cheque 10% de desconto
[1]>> À vista no no débito 5% de desconto
[2]>> Até 2x no crédito preço normal
[3]>> 3x ou mais 20% de juros  \n\n''')

opcao = int(input(''))

if   opcao == 0:
    print(f'\nO preço do produto que era R${preco:.2f} com o desconto de 10% fica: R${preco - (preco * 0.10):.2f} \n')

elif opcao == 1:
    print(f'\nO preço do produto que era R${preco:.2f} com o desconto de 5% fica: R${preco - (preco *0.05):.2f} \n ')

elif opcao == 2:
    print(f'\nO preço do produto que é: R${preco:.2f}')

elif opcao == 3:
    print(f'\nO preço do produto que era R${preco:.2f} com os juros de 20% fica: R${preco + (preco *0.20):.2f} \n')
else :
    print('\n\nOpção inválida')


sleep(0.9)
print(f'\n\n')
sleep(0.05)
print(f'\033[41m{" Programa encerrado ":^90}\033[m')
sleep(0.05)
print(f'\n\n\n')