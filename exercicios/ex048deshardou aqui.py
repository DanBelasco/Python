


total = 0 
x = 0
for c in range(1,501,2):
    if c % 3 == 0:
        total = total + c
        x = x +1

print(f'\nA quantidade de vezes que o numero atendeu os requisitos foi: {x}')
print(f'\n O total da soma foi:{total}')