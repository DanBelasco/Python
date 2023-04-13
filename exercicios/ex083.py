#analizar se tem o mesmo numero de parenteses na expressã
aberto = 0
fechado = 0
mmo =[]
print('\n\n\n')
lol = str(input('Digite uma expressão >>>  '))

mmo.append(lol)

for posição, conteudo in enumerate(mmo[0]):
    if conteudo == '(':
        aberto = aberto + 1
    
for posição , conteudo in enumerate(mmo[0]):
    if conteudo == ')':
        fechado = fechado + 1

print('\n')
if aberto == fechado:
    print(f'A expressão pode ser executa pois tem o mesmo nuemero de parenteses ')
elif aberto > fechado:
    print(f'expressão errada esta faltanto {aberto - fechado} ")" '  )
else:
    print(f'expressão errada esta faltanto {fechado - aberto}  "(" ')

print('\n\n')



