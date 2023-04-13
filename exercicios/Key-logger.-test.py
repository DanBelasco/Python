from random import randint
from datetime import datetime
from time import sleep

contador = 0
dia = datetime.today().date()  # Recebe o dia atual

listaõ =[] #cria Lista
      
listaõ.append(f'DATA: {dia}') # Adiciona na lista o dia atual 

while True:
    hora = datetime.today().time()  #loop que recebe a cada volta um numero random de 0 a 100 e a hora atual
    key = str(input())

    listaõ.append(f'Hora: [{hora}], Conteudo: {key} ')

    

    contador = contador + 1 # contador de controle do loop
    
    sleep(0.1) # Delay muito importante para saber as divisões de tempo da leitura
    #            Quanto menor o  delay menor o divisor de leitura e maior tempo 
    
    if contador == 10: # O contador tem o papel de tempo de duração  do programa
        break



listaõ2 = '\n'.join(listaõ) # join para formatar as strings pulando linhas

# print(listaõ2) # print de teste

arqTexto = open('G:\Meu Drive\Códigos\Python\Curso em Vídeo\exercicios\Key-Log-Test.txt', 'w') #criando o arquivo datalog

arqTexto.writelines(f'{listaõ2}') # escrevendo as strings dentro do arquivo criado