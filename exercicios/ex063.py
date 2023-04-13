#somar o numero anterior ao ultimo resulta no proximo
c = 0 
proximo = 1
anterior = 0
termos = int(input('Quantos termos você deseja mostrar?  \n\n >>>> '))

while c != termos:
    print(f'{anterior}, {proximo}' , end=", ")
    anterior = anterior + proximo
    proximo = proximo + anterior

    c = c + 1