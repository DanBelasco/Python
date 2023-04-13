

from modulosss.uteis.matematica.operacoes import ipo,fat

from modulosss.uteis.encerra import cabô

"""
posso importar funçoes de modulos e pacotes (libs) do diretorio da pasta raiz do projeto.
Para isso tenho que chamar a mesma respeitando a hierarquia das pastas igualmente no windows. 
* EXEMPLO:   " from c:\arquivosdeprogramas\steam\games import skyrim "

Para o Python usamos o ponto "." como sempardor no lugar da barra. ficando assim:
* EXEMPLO:   " from c:.arquivosdeprogramas.steam.games import skyrim "

dessa maneira posso chamar a função direto pelo nome, sem precisar usar seu diretório como
caminho toda vez que precisar dela.

Caso precise, a Função ainda pode receber um outro nome para facilitar a sua chamada 
utilizando o comando "as" antes do novo nome.

* Exemplo: " from c:.arquivosdeprogramas.steam.games import skyrim as sk "

Agora quando precisar usar no código principal é so escrever com o nome reduzido

* EXEMPLO   " jogo = sk() "

"""

#############

num = int(input('\n\nDigite o numero que deseja o fatorial >>> '))

fatorial  = fat(num)

print(f'\n\n O fatorial de {num} é {fatorial}  ')


prim = float(input('\n\n Cateto A:  '))
segu = float(input('\n Cateto B:  '))

total = ipo(prim, segu)

print(f'\nA hipotenusa é {total:.2f}')


cabô()