matrix  = [[],[],[]]
contA = 0 
contB = 0

print('\n\n')
for d in range(0,9):
    num = int(input(f'Digite uma valor para o ponto [{contA} , {contB}]  da matrix:  >>> '))
    contB = contB + 1
    if d <=2:
        matrix[0].append(num)
        if d >=2:
            contB =0
            contA =1

    elif d <=5:
        matrix[1].append(num)
        if d >= 5:
            contB = 0
            contA =2
       
    elif d <=8:
        matrix[2].append(num)
        contA = 2
            
    d = d + 1

print('\n')
for l in range(0,len(matrix[0])):
    
    for p in range(0,len(matrix)):
        if l == 1 and p == 0:
            print('')
        elif l == 2 and p == 0:
            print('')
        print(f' [  {matrix[l][p]:^4}  ]' ,end='')
        

print('\n\n')
print(f'\033[41m{" Programa encerrado ":^90}\033[m')
print('\n\n\n')