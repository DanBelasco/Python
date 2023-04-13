


aberto =0 
fechado = 0
pilha = []

print('\n\n\n')

expre = str(input('Digite uma expressão  \n >>>  '))

for c in range(0, len(expre)):
    if expre[c] == '(':
        pilha.append('(')
    elif expre[c] == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
    
if len(pilha) ==0 :
    print('\n\nexpressão valida')
else:
    print('\n\nExpressão errada')


