
def alunos(*notas, status = False):

    '''
    == Função Alunos ==
    ------------------------------------------------------------------------
    Função Alunos tem como objetivo retormar um dicionário contendo:
    *Total de notas
    *Máximo valor de notas
    *Mínimo valor de notas
    *Média de notas
    *Situação Lieteral do aluno
    
    <parametro> *notas: Lista com notas dos alunos. (*) volume indefinido
    <parametro> status: quando em True, adiciona ao dicionário a situação
      lieteral que o aluno se encontra. (false) NF
    -------------------------------------------------------------------------
    
    '''
    
    dic = {}
    maior = meno = med = 0
    sit = ''

    dic["total"] = len(notas)

    for c in range(0, len(notas)):
        if c == 0:
            maior = notas[c]
        if notas[c] > maior:
            maior = notas[c]
        if c == 0:
            meno = notas[c]
        if notas[c] < meno:
            meno = notas[c]

    dic['maior'] = maior
    dic['menor'] = meno

    med = (sum(notas) / len(notas))

    dic['media'] = med

    if med > 7:
        sit = 'Ótimo'

    elif med == 7:
        sit = 'Boa'

    elif med >=5 and med <7:
        sit = 'Regular'

    elif med < 5:
        sit = 'Ruim'

    if status == True:
        dic['Situação'] = sit

    return dic


###################
resposta = alunos(9,5.6,9,10,4.5,5.5, status = True)

print(resposta)

#help(alunos)


print('\n')
print(f'\033[41m{" Programa encerrado ":^90}\033[m')
