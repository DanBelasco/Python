
from time import sleep

print('\n\nContagem regressiva para os fogos!\n')
sleep(2)
contagem = 10
for c in range(0,11):
    print(contagem)
    sleep(0.5)
    print('\n')
    contagem = contagem - 1
print('\n\033[7mBOOOOOOOOOOMMMMM!!!!!!\033[m\n')