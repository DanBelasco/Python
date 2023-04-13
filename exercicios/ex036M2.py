from time import sleep

sleep(0.05)
print(f'\n\n\n{"":=^90}')
sleep(0.05)
print(f'\033[7m{" INICIALIZANDO ":^90}\033[m')
sleep(0.05)
print(f'{"":=^90}\n')
sleep(0.05)
print(f'\n\033[36m{" Programa para analisar financiamento de imóvel ":=^90}\033[m\n\n')
sleep(0.05)

vc = float(input('\nDigite o valor do imóvel: \n >>> ')) #valor da casa
sl = float(input('\nDigite o valor da renda: \n >>> ')) #valor do salário
an = float(input('\nDigite em quantos anos o cliente dejesa pagar: \n >>> ')) #quanto anos para pagar

vm = vc / (an * 12) #valor da mensalidade

if vm < (sl * 0.30):
    print(f'\n\033[42mParabéns seu finaciamento foi aprovado nas seguintes condições!\033[m')
    print(f'\nPara nao exeder os 30 % da sua renda e conseguir terminar o pagamento\nem {an} anos')
    print(f'\nO imóvel avaliado em R${vc:.0f}. Terá o valor da mensalidade de:\033[43m R${vm:.2f}\033[m\n')

else:
    print(f'\n\033[31mInfelizmente seu financiamento não pode ser realizado, pois a mensalidade\ndo imóvel ultrapassa os 30% de sua renda!\033[m')
    print(f'\n\033[7mDICA\033[m')
    print(f'\n\nTente um imóvel mais barato ou juntar sua renda com outra pessoa.')

sleep(0.9)
print(f'\n\n')
sleep(0.05)
print(f'\033[7m{" Programa encerrado ":^90}\033[m')
sleep(0.05)
print(f'\n\n\n')
