# 5 primeiros colocados
# o s ultimos 4
# ordem alfabetica
# onde esta chapeco?

from operator import index
from turtle import pos


lista = ('Palmeiras','Internacional','Flamengo','Fluminense',
'Corinthians','Athletico-PR','Atlético-MG','América-MG','Goiás',
'Santos','Bragantino','Botafogo','São Paulo','Ceará','Fortaleza',
'Coritiba','Cuiabá','Avaí','Atlético Goianiense','Chapecoense')
c=1
for t in lista:
    print(c, t,)
    c = c+1
print(f'\n\n\033[33mOs 5 primeiros colocados da tabela são:\033[m\n\n {lista[0:5] } ')

print(f'\n\n\033[33mOs 4 ultimos colocados são:\033[m\n\n {lista[20:15:-1]}')
nova = sorted(lista)
print(f'\n\n\033[33mOrdem alfabética dos clubes na primeiro divisão:\033[m \n\n')
for f in nova:
    print(f)

print(f'\n\n\033[32mChapecoense está na posição\033[m  {lista.index("Chapecoense") +1 }º ')