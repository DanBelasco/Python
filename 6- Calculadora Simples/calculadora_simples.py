# Esse programa tem como objetivo cirar uma calculadora simples de oprações básicas com interface simples de navegação
from math import sqrt
from tkinter import*

janela1 = Tk()

janela1.title('Calculadora de oprações básicas')

#Tela de interface 
tela = Entry(janela1, width=12, font=('arial',35)  ,border= 4,) # conf de janela de visualização
tela.grid(row= 0, column=0 , columnspan= 4 ,padx=2,pady=9,)


#função dos botões

def botao(numero):  #mostrar o digito clicado 
    atual = tela.get()
    tela.delete(0,END)
    tela.insert(0, str(atual) + str(numero))
  


def botsomar():  #armazena o primeiro digito da soma
    global atualdatela
    global mat
    mat = 'somar'
    atualdatela = tela.get()
    tela.delete(0,END)
        

def botigual():  
    atual2 = tela.get()
    tela.delete(0,END)
    if mat == 'somar':
        total = (float(atualdatela) + float(atual2))  #check para saber qual a operação será realizada

    if mat == 'subtrair':
        total = (float(atualdatela) - float(atual2))

    if mat == 'multiplicar':
        total = (float(atualdatela) * float(atual2))

    if mat == 'dividir':
        total = (float(atualdatela) / float(atual2))

    if mat == 'pote':
        total = (pow (float(atualdatela),float(atual2)))

    tela.insert(0, total)


def mult():
    global atualdatela
    global mat
    mat = 'multiplicar'
    atualdatela = tela.get()
    tela.delete(0,END)
    


def sub():
    global atualdatela
    atualdatela = tela.get()
    if len(atualdatela) == 0 :   #conferindo se ja existe digitos na tela para poder adicionar o simbolo de Sub na frente
        tela.insert(0,'-')
    else:
        global mat
        mat = 'subtrair'          #caso ja tenha, deve prosseguir com a operação normalmente
    
        tela.delete(0,END)
    


def div():
    global atualdatela
    global mat
    mat = 'dividir'
    atualdatela = tela.get()
    tela.delete(0,END)
    

def pote():
    global atualdatela
    global mat
    mat = 'pote'
    atualdatela = tela.get()
    tela.delete(0,END)

def raiz():
    global atualdatela
    atualdatela = tela.get()
    tela.delete(0,END)
    total = sqrt(float(atualdatela))
    tela.insert(0, total)

def porcem():
    global atualdatela
    global mat
    atual2 = tela.get()
    tela.delete(0,END)
    if mat == 'somar':
        total = (((float(atualdatela)/100)* float(atual2) ) + float(atualdatela) )

    if mat == 'subtrair':
        total = (float(atualdatela) - ((float(atualdatela)/100)* float(atual2) ))

    if mat == 'multiplicar':
        total = (float(atualdatela) * (float(atual2) /100))

    if mat == 'dividir':
        total = (float(atualdatela) / (float(atual2) /100))

    tela.insert(0, total)

def clear():  #limpa a tela
    tela.delete(0,END)
    tela.insert(0,'')


# Config de botoes
botaoLimpar = Button(janela1, text='C',padx=30, pady=10, border=3, command= clear, bg='#edb9b2',width=1, height=1) 
botaoLimpar.grid(row= 1 ,column=0 )

botao1 = Button(janela1, text='1',padx=30,pady=10, border=3, command= lambda: botao(1),width=1, height=1, activebackground="#c0edf0",background='#dce3e3' )
botao1.grid(row= 1 ,column=1 )

botao2 = Button(janela1, text='2',padx=30,pady=10, border=3, command= lambda: botao(2),width=1, height=1, activebackground="#c0edf0",background='#dce3e3')
botao2.grid(row= 1 ,column=2 )

botao3 = Button(janela1, text='3',padx=30,pady=10, border=3, command= lambda: botao(3),width=1, height=1, activebackground="#c0edf0",background='#dce3e3')
botao3.grid(row= 2 ,column=0 )

botao4 = Button(janela1, text='4',padx=30,pady=10, border=3, command= lambda: botao(4),width=1, height=1, activebackground="#c0edf0",background='#dce3e3')
botao4.grid(row= 2 ,column=1 )

botao5 = Button(janela1, text='5',padx=30,pady=10, border=3, command= lambda: botao(5),width=1, height=1, activebackground="#c0edf0",background='#dce3e3')
botao5.grid(row= 2 ,column=2 )
 
botao6 = Button(janela1, text='6',padx=30,pady=10, border=3, command= lambda: botao(6),width=1, height=1, activebackground="#c0edf0",background='#dce3e3')
botao6.grid(row= 3 ,column=0 )

botao7 = Button(janela1, text='7',padx=30,pady=10, border=3, command= lambda: botao(7),width=1, height=1, activebackground="#c0edf0",background='#dce3e3')
botao7.grid(row= 3 ,column=1 )

botao8 = Button(janela1, text='8',padx=30,pady=10, border=3, command= lambda: botao(8),width=1, height=1, activebackground="#c0edf0",background='#dce3e3')
botao8.grid(row= 3 ,column=2 )

botao9 = Button(janela1, text='9',padx=30,pady=10, border=3, command= lambda: botao(9),width=1, height=1, activebackground="#c0edf0",background='#dce3e3')
botao9.grid(row= 4 ,column=0 )

botao0 = Button(janela1, text='0',padx=30,pady=10, border=3, command= lambda: botao(0),width=1, height=1, activebackground="#c0edf0",background='#dce3e3')
botao0.grid(row= 4 ,column=1 )

botaoponto = Button(janela1, text='.',padx=30,pady=10, border=3, command= lambda: botao("."),width=1, height=1, activebackground="#c0edf0",background='#dce3e3')
botaoponto.grid(row= 4 ,column=2 )

botaosoma = Button(janela1, text='+',padx=30,pady=10, border=3, command= botsomar,width=1, height=1, activebackground="#c0edf0",background='#dce3e3')
botaosoma.grid(row= 3 ,column=3 ,  )

botaosub = Button(janela1, text='-',padx=30,pady=10, border=3, command= sub,width=1, height=1, activebackground="#c0edf0",background='#dce3e3')
botaosub.grid(row= 2 ,column=3  )

botaomult = Button(janela1, text='*',padx=30,pady=10, border=3, command=mult,width=1, height=1, activebackground="#c0edf0",background='#dce3e3')
botaomult.grid(row= 1 ,column=3  )

botaodiv = Button(janela1, text='/',padx=30,pady=10, border=3, command= div,width=1, height=1, activebackground="#c0edf0",background='#dce3e3')
botaodiv.grid(row= 4 ,column=3  )

botaoigual = Button(janela1, text='=',padx=30,pady=10, border=3, command= botigual ,width=1, height=1, activebackground="#c0edf0",background='#dce3e3')
botaoigual.grid(row= 5 ,column=3 )

botaopot = Button(janela1, text='x^',padx=30,pady=10,border=3, command= pote , width=1, height=1, activebackground="#c0edf0",background='#dce3e3')
botaopot.grid(row= 5 ,column=0 )

botaoraiz = Button(janela1, text='√',padx=30,pady=10, border=3, command= raiz ,width=1, height=1 , activebackground="#c0edf0",background='#dce3e3')
botaoraiz.grid(row= 5 ,column=1)

botaoporcem = Button(janela1, text='%',padx=30,pady=10, border=3, command= porcem ,width=1, height=1 , activebackground="#c0edf0",background='#dce3e3')
botaoporcem.grid(row= 5 ,column=2 )
 

################################
janela1.mainloop()