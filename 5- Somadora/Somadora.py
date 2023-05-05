# Esse programa tem como objetivo cirar uma calculadora de soma simples com interface basica de navegação

from tkinter import*

janela1 = Tk()

janela1.title('Calculadora de somar')

#Tela de interface 

tela = Entry(janela1, width=46 , border= 3,) # conf de janela de visualização
tela.grid(row= 0, column=0 , columnspan= 3,padx=2,pady=9,)


#função dos botões

def botao(numero):  #mostrar o digito clicado 
    atual = tela.get()
    tela.delete(0,END)
    tela.insert(0, str(atual) + str(numero))
  


def botsomar():  #armazena o primeiro digito da soma
    global atualdatela
    atualdatela = tela.get()
    tela.delete(0,END)
    return atualdatela
    

def botigual():  #mostra o resultado da soma com o segundo digito
    atual2 = tela.get()
    tela.delete(0,END)
    total = (int(atualdatela) + int(atual2))
    tela.insert(0, total)
    


def clear():  #limpa a tela
    tela.delete(0,END)
    tela.insert(0,'')


# Config de botoes
botaoLimpar = Button(janela1, text='Limpar',padx=120, pady=5, border=3, command= clear, bg='#edb9b2')
botaoLimpar.grid(row= 1 ,column=0 , columnspan= 3)

botao1 = Button(janela1, text='1',padx=40,pady=20, border=3, command= lambda: botao(1))
botao1.grid(row= 2 ,column=0 )

botao2 = Button(janela1, text='2',padx=40,pady=20, border=3, command= lambda: botao(2))
botao2.grid(row= 2 ,column=1 )

botao3 = Button(janela1, text='3',padx=40,pady=20, border=3, command= lambda: botao(3))
botao3.grid(row= 2 ,column=2 )

botao4 = Button(janela1, text='4',padx=40,pady=20, border=3, command= lambda: botao(4))
botao4.grid(row= 3 ,column=0 )

botao5 = Button(janela1, text='5',padx=40,pady=20, border=3, command= lambda: botao(5))
botao5.grid(row= 3 ,column=1 )
 
botao6 = Button(janela1, text='6',padx=40,pady=20, border=3, command= lambda: botao(6))
botao6.grid(row= 3 ,column=2 )

botao7 = Button(janela1, text='7',padx=40,pady=20, border=3, command= lambda: botao(7))
botao7.grid(row= 4 ,column=0 )

botao8 = Button(janela1, text='8',padx=40,pady=20, border=3, command= lambda: botao(8))
botao8.grid(row= 4 ,column=1 )

botao9 = Button(janela1, text='9',padx=40,pady=20, border=3, command= lambda: botao(9))
botao9.grid(row= 4 ,column=2 )

botao0 = Button(janela1, text='0',padx=40,pady=20, border=3, command= lambda: botao(0))
botao0.grid(row= 5 ,column=0 )

botaosoma = Button(janela1, text='+',padx=60,pady=20, border=3, command= lambda: botsomar())
botaosoma.grid(row= 5 ,column=1 , columnspan=2, sticky=W)

botaoigual = Button(janela1, text='=',padx=18,pady=20, border=3, command= botigual )
botaoigual.grid(row= 5 ,column=2 , columnspan=2, sticky=E)

 

################################
janela1.mainloop()