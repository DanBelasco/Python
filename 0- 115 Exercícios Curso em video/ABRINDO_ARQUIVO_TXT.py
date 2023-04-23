

def mostralinha2():
    oarquivo = open('lol.txt','r')
    oConteudo = oarquivo.readlines()

    for linha in oConteudo:
        separador = linha.split(';')
        separador[1] = separador[1].replace('\n','')
        print(f'{separador[0]} {separador[1]}')

mostralinha2()