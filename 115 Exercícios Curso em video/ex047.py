print('\nprimeiro método\n')

for cont in range(0,51,2):
    print(cont)

print('\n\nSegundo médoto\n')
resultado = 0
numero =0

for cont2 in range(0,51):
    resultado = numero % 2
    if resultado == 0:
        print(numero)
    numero = numero + 1
