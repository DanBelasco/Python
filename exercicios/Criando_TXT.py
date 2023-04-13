
listaDeBolos = ['Bolo de cenoura','Bolo de chocolate','Bolo da Aipim','Bolo de fubá cremoso','Bolo formigueiro','Bolo de MILHO''Bolo de cenoura','Bolo de chocolate','Bolo da Aipim','Bolo de fubá cremoso','Bolo formigueiro','Bolo de cenoura','Bolo de chocolate','Bolo da Aipim','Bolo de fubá cremoso','Bolo formigueiro','Bolo de cenoura','Bolo de chocolate','Bolo da Aipim','Bolo de fubá cremoso','Bolo formigueiro']



listaDeBolos2 = ' '

listaDeBolos2 = '\n'.join(listaDeBolos)


arqTexto = open('G:\Meu Drive\Códigos\Python\Curso em Vídeo\exercicios\txtZvaitomarnocu.txt', 'a') # 'a' Serve para bubescrever mesmo ja tendo algo escrito no arquivo TXT

arqTexto.writelines(f'{listaDeBolos2}')