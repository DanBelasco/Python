import matematica.operacoes

fatorial = matematica.operacoes.fat(5)

print(fatorial)

'''
Adicionar o arquivo __init__.py na mesma pasta do diretorio do projeto, faz com que o 
o arquivo que irá rodar o codigo limpo, possa importar os recuros (funçoes) do modulo 
"uteis". transformando assim uma pasta em pacote.(LIB) 
podendo importar recursos diretos
'''
#####################

from matematica.operacoes import fat

fatorial_2 = fat(4)
print(fatorial_2)
'''
Caso a Lib não seja muito grande. pode-se importar tudo com o asteristico e não usar mais 
a nomeclatura completa para chamar a função.

'''