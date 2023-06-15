from tkinter import messagebox
from tkinter import*
import tkinter as tk
import sqlite3


def mensAbertura():
    jan5 = tk.Tk()
    labaum = tk.Label(jan5, text='D&D Data Book',font=('Times New Roman','60'), fg='RED', bg='white', highlightthickness=9)
    labaum.pack()

    jan5.overrideredirect(True)
    jan5.geometry("+490+150")
    jan5.wm_attributes("-topmost", True)
    jan5.wm_attributes("-disabled", True)
    jan5.wm_attributes("-transparentcolor", "white")
    
    jan5.after(1000, jan5.destroy)
    jan5.mainloop()

mensAbertura()

def armas():

    janela1 = Toplevel()
    janela1.title('Gerador de Armamento' )
    janela1.iconbitmap('G:/Meu Drive/Códigos/Python/TKinter/D&D/p2.ico')  ### <<< imagem de icone
    #janela1.geometry('870x679')

    janela1.overrideredirect(False)
    janela1.geometry("+200+20")

    
    
    cordefundo = '#183d1e'
    cordobotao = '#19594b'
    cordeletra2 = '#7dff93'
    cordeletra = '#ffffff'

    janela1.configure(background=cordefundo)
    janela1.resizable(width=False, height=False)
   
    janela1.grab_set()
    janela1.deiconify()

   
    lista_de_nomes=['ID', 'nome', 'Tipo', 'Tipo_de_ataque', 'habilidade_especial', 'custo_de_estamina', 'peso', 'atc_fisico', 'atc_magico', 'atc_fogo', 'atc_raio', 'atc_sagrado', 'atc_critico', 'def_fisico', 'def_magico', 'def_fogo', 'def_raio', 'def_sagrado', 'def_bonus', 'esc_forca', 'esc_dex', 'esc_int', 'esc_fe', 'esc_arcano', 'att_req_forca', 'att_req_dex', 'att_req_int', 'att_req_fe', 'att_req_arcano', 'passeffect']


    def limpa(idd):
        global campoID
        campoID = ID.get().strip()
        conn = sqlite3.connect('jogo.db')
        cur = conn.cursor()
        

        cur.execute(f" DELETE FROM Armas WHERE ID == '{campoID}' ; ")
        conn.commit()
        ######################
    def menssagem_vazio():
        jan3 = tk.Tk()
        labaum = tk.Label(jan3, text='CAMPO ID VAZIO!',font=('Times New Roman','60'), fg='YELLOW', bg='white')
        labaum.pack()

        jan3.overrideredirect(True)
        jan3.geometry("+390+50")
        jan3.wm_attributes("-topmost", True)
        jan3.wm_attributes("-disabled", True)
        jan3.wm_attributes("-transparentcolor", "white")
        
        jan3.after(1500, jan3.destroy)
        jan3.mainloop()
        ######################
    def menssagem_errado():
        jan2 = tk.Tk()
        labaum = tk.Label(jan2, text='CAMPO ID INVÁLIDO',font=('Times New Roman','60'), fg='YELLOW', bg='white')
        labaum.pack()

        jan2.overrideredirect(True)
        jan2.geometry("+390+50")
        jan2.wm_attributes("-topmost", True)
        jan2.wm_attributes("-disabled", True)
        jan2.wm_attributes("-transparentcolor", "white")
        
        jan2.after(1500, jan2.destroy)
        jan2.mainloop()
        ######################
    def menssagem_errado2():
        
        jan3 = tk.Tk()
        labaum = tk.Label(jan3, text='WARNING!',font=('Times New Roman','60'), fg='YELLOW', bg='white')
        labaum.pack()

        jan3.overrideredirect(True)
        jan3.geometry("+390+50")
        jan3.wm_attributes("-topmost", True)
        jan3.wm_attributes("-disabled", True)
        jan3.wm_attributes("-transparentcolor", "white")
        
        jan3.after(1900, jan3.destroy)
        ###################### 
    def menssagem3(qualarea):
        jan6 = tk.Tk()
        labaum = tk.Label(jan6, text=qualarea ,font=('Times New Roman','60'), fg='YELLOW', bg='white')
        labaum.pack()

        jan6.overrideredirect(True)
        jan6.geometry("+390+50")
        jan6.wm_attributes("-topmost", True)
        jan6.wm_attributes("-disabled", True)
        jan6.wm_attributes("-transparentcolor", "white")
        
        jan6.after(1000, jan6.destroy)

    def filtro_vazio():    
        if nome.get() == '':
            menssagem3('Nome')
        elif Tipo.get() == '':
            menssagem3('Tipo')
        elif Tipo_de_ataque.get() == '':
            menssagem3('Tipo ataque')
        elif habilidade_especial.get() == '':
            menssagem3('Habilidade')
        elif custo_de_estamina.get() == '':
            menssagem3('Custo')
        elif peso.get() == '':
            menssagem3('Peso')
        else:
            filtro_aplica()



    def filtro_aplica():
        
        global caixa_de_pergunta
        
        conn = sqlite3.connect('jogo.db')
        cur = conn.cursor()
        #######
        
        cur.execute("SELECT id FROM armas; ")
        IDcadastrados = cur.fetchall()
        campoID = ID.get().strip()


        if campoID == '' :
            menssagem_vazio()

        elif campoID.isnumeric() == False:
            menssagem_errado()

        elif str(campoID) in str(IDcadastrados):
            menssagem_errado2()
            base.withdraw()
            caixa_de_pergunta = messagebox.askyesno('WARNING!','O ID informado JÁ existe!\nDeseja substituí-lo?')
            
            if caixa_de_pergunta == 1:
                base.deiconify()
                limpa(campoID)
                aplicar()
            
        else: 
            base.deiconify()
            
                
            
    #############################
        conn.commit()
        conn.close()
        ######################

    def filtro_Busca():
        
        global caixa_de_pergunta
        
        conn = sqlite3.connect('jogo.db')
        cur = conn.cursor()
        #######
        
        cur.execute("SELECT id FROM armas; ")
        IDcadastrados = cur.fetchall()
        campoID = ID.get().strip()


        if campoID == '' :
            menssagem_vazio()

        elif campoID.isnumeric() == False:
            menssagem_errado()

        elif str(campoID) not in str(IDcadastrados):
            menssagem_errado2()
            
            base.withdraw()
            caixa_de_pergunta = messagebox.askyesno('WARNING!','O ID informado NÃO existe!\nDeseja criá-lo?')
            janela1.grab_set()
            janela1.deiconify()


            if caixa_de_pergunta == 1:
                base.deiconify()
                None 
            else: 
                base.deiconify()
                apaga()
                
        else: 
            consultar()

    def nomes():
        '''


    ID
    nome
    Tipo
    Tipo_de_ataque
    habilidade_especial
    custo_de_estamina
    peso
    atc_fisico
    atc_magico
    atc_fogo
    atc_raio
    atc_sagrado
    atc_critico
    def_fisico
    def_magico
    def_fogo
    def_raio
    def_sagrado
    def_bonus
    esc_forca
    esc_dex
    esc_int
    esc_fe
    esc_arcano
    att_req_forca
    att_req_dex
    att_req_int
    att_req_fe
    att_req_arcano
    passeffect

    'ID', 'nome', 'Tipo', 'Tipo_de_ataque', 'habilidade_especial', 'custo_de_estamina', 'peso', 'atc_fisico', 'atc_magico', 'atc_fogo', 'atc_raio', 'atc_sagrado', 'atc_critico', 'def_fisico', 'def_magico', 'def_fogo', 'def_raio', 'def_sagrado', 'def_bonus', 'esc_forca', 'esc_dex', 'esc_int', 'esc_fe', 'esc_arcano', 'att_req_forca', 'att_req_dex', 'att_req_int', 'att_req_fe', 'att_req_arcano', 'passeffect'


    '''
        return

    def aplicar():

        conn = sqlite3.connect('jogo.db')
        cur = conn.cursor()
        ##################
        
        cur.execute("INSERT INTO Armas VALUES (:ID, :nome, :Tipo, :Tipo_de_ataque, :habilidade_especial, :custo_de_estamina, :peso, :atc_fisico, :atc_magico, :atc_fogo, :atc_raio, :atc_sagrado, :atc_critico, :def_fisico, :def_magico, :def_fogo, :def_raio, :def_sagrado, :def_bonus, :esc_forca, :esc_dex, :esc_int, :esc_fe, :esc_arcano, :att_req_forca, :att_req_dex, :att_req_int, :att_req_fe, :att_req_arcano, :passeffect, :atc_bonus )",
        {'ID': ID.get(),
        'nome': nome.get(),
        'Tipo': Tipo.get(),
        'Tipo_de_ataque': Tipo_de_ataque.get(),
        'habilidade_especial': habilidade_especial.get(),
        'custo_de_estamina': custo_de_estamina.get(),
        'peso': peso.get(),
        'atc_fisico': atc_fisico.get(),
        'atc_magico': atc_magico.get(),
        'atc_fogo': atc_fogo.get(),
        'atc_raio': atc_raio.get(),
        'atc_sagrado': atc_sagrado.get(),
        'atc_critico': atc_critico.get(),
        'def_fisico': def_fisico.get(),
        'def_magico': def_magico.get(),
        'def_fogo': def_fogo.get(),
        'def_raio': def_raio.get(),
        'def_sagrado': def_sagrado.get(),
        'def_bonus': def_bonus.get(),
        'esc_forca': esc_forca.get(),
        'esc_dex': esc_dex.get(),
        'esc_int': esc_int.get(),
        'esc_fe': esc_fe.get(),
        'esc_arcano': esc_arcano.get(),
        'att_req_forca': att_req_forca.get(),
        'att_req_dex': att_req_dex.get(),
        'att_req_int': att_req_int.get(),
        'att_req_fe': att_req_fe.get(),
        'att_req_arcano': att_req_arcano.get(),
        'passeffect': passeffect.get(), 
        'atc_bonus' : atc_fisico.get()} )
        ##################
        conn.commit()
        conn.close()

        apaga()
        menssagem()

    def menssagem():
        jan2 = tk.Tk()
        labaum = tk.Label(jan2, text='SALVO COM SUCESSO!',font=('Times New Roman','60'), fg='#42d64c', bg='white',highlightthickness=9)
        labaum.pack()

        jan2.overrideredirect(True)
        jan2.geometry("+190+50")
        jan2.wm_attributes("-topmost", True)
        jan2.wm_attributes("-disabled", True)
        jan2.wm_attributes("-transparentcolor", "white")
        
        jan2.after(1500, jan2.destroy)
        jan2.mainloop()

    def apaga():
        

        ID.delete(0,END)
        nome.delete(0,END)
        Tipo.delete(0,END)
        Tipo_de_ataque.delete(0,END)
        habilidade_especial.delete(0,END)
        custo_de_estamina.delete(0,END)
        peso.delete(0,END)
        atc_fisico.delete(0,END)
        atc_magico.delete(0,END)
        atc_fogo.delete(0,END)
        atc_raio.delete(0,END)
        atc_sagrado.delete(0,END)
        atc_critico.delete(0,END)
        def_fisico.delete(0,END)
        def_magico.delete(0,END)
        def_fogo.delete(0,END)
        def_raio.delete(0,END)
        def_sagrado.delete(0,END)
        def_bonus.delete(0,END)
        esc_forca.delete(0,END)
        esc_dex.delete(0,END)
        esc_int.delete(0,END)
        esc_fe.delete(0,END)
        esc_arcano.delete(0,END)
        att_req_forca.delete(0,END)
        att_req_dex.delete(0,END)
        att_req_int.delete(0,END)
        att_req_fe.delete(0,END)
        att_req_arcano.delete(0,END)
        passeffect.delete(0,END)

    def consultar():
        conn = sqlite3.connect('jogo.db')
        cur = conn.cursor()

        idescolhido= ID.get()
    
        cur.execute(f"SELECT*  FROM Armas WHERE ID = {idescolhido};    ")
        procurajogo= cur.fetchall()
        
        apaga()
        #nome.insert(0,procurajogo[0][1])
        
        ID.insert(0,(procurajogo[0]                 [0]))
        nome.insert(0,(procurajogo[0]               [1]))
        Tipo.insert(0,(procurajogo[0]               [2]))
        Tipo_de_ataque.insert(0,(procurajogo[0]     [3]))
        habilidade_especial.insert(0,(procurajogo[0][4]))
        custo_de_estamina.insert(0,(procurajogo[0]  [5]))
        peso.insert(0,(procurajogo[0]               [6]))
        atc_fisico.insert(0,(procurajogo[0]         [7]))
        atc_magico.insert(0,(procurajogo[0]         [8]))
        atc_fogo.insert(0,(procurajogo[0]           [9]))
        atc_raio.insert(0,(procurajogo[0]           [10]))
        atc_sagrado.insert(0,(procurajogo[0]        [11]))
        atc_critico.insert(0,(procurajogo[0]        [12]))
        def_fisico.insert(0,(procurajogo[0]         [13]))
        def_magico.insert(0,(procurajogo[0]         [14]))
        def_fogo.insert(0,(procurajogo[0]           [15]))
        def_raio.insert(0,(procurajogo[0]           [16]))
        def_sagrado.insert(0,(procurajogo[0]        [17]))
        def_bonus.insert(0,(procurajogo[0]          [18]))
        esc_forca.insert(0,(procurajogo[0]          [19]))
        esc_dex.insert(0,(procurajogo[0]            [20]))
        esc_int.insert(0,(procurajogo[0]            [21]))
        esc_fe.insert(0,(procurajogo[0]             [22]))
        esc_arcano.insert(0,(procurajogo[0]         [23]))
        att_req_forca.insert(0,(procurajogo[0]      [24]))
        att_req_dex.insert(0,(procurajogo[0]        [25]))
        att_req_int.insert(0,(procurajogo[0]        [26]))
        att_req_fe.insert(0,(procurajogo[0]         [27]))
        att_req_arcano.insert(0,(procurajogo[0]     [28]))
        passeffect.insert(0,(procurajogo[0]         [29]))

        return


    q11 = LabelFrame(janela1, text='Geral',  padx= 42 , pady= 30, background= cordefundo, foreground=cordeletra2, font=('Sylfaen',20) )
    q11.grid( row=1 , column= 0 ,sticky=W , )

    q0 = LabelFrame(janela1, text='Foto da arma',  padx= 45 , pady= 30, background=cordefundo, foreground=cordeletra2)
    q0.grid( row=1 , column= 1 , sticky=E  )

    q2 = LabelFrame(janela1, text='Attack Power', padx= 180 , pady= 20, background=cordefundo, foreground=cordeletra2, font=('Sylfaen',13)) 
    q2.grid( row=3 , column= 0, sticky=W ,columnspan=2 , )

    q3 = LabelFrame(janela1, text='Guarded Damage Negation', padx= 100 , pady= 20, background=cordefundo, foreground=cordeletra2, font=('Sylfaen',13))
    q3.grid( row=3 , column= 1, sticky=W )

    q4 = LabelFrame(janela1, text='Attribute Scaling',  padx= 145 , pady= 20 , background=cordefundo, foreground=cordeletra2, font=('Sylfaen',13))
    q4.grid( row=4 , column= 0, sticky=W ,padx=5)

    q5 = LabelFrame(janela1, text='Attribute Required', padx= 76 , pady= 20, background=cordefundo, foreground=cordeletra2, font=('Sylfaen',13))
    q5.grid( row=4 , column= 1, columnspan=2, sticky=W,)

    q6 = LabelFrame(janela1, text='Passive Effects',  padx= 93 , pady= 10 , background=cordefundo, foreground=cordeletra2, font=('Sylfaen',13))
    q6.grid( row=5 , column= 0 , columnspan=2 ,sticky=W )

    q7 = LabelFrame(janela1, text='!',  padx= 98 , pady= 7.5 , background=cordefundo, foreground=cordeletra2, font=('Sylfaen',13))
    q7.grid( row=5 , column= 1 , columnspan=2 ,sticky=W )

    

    ###############################
    #Criando banco de dados ou conectanto á uma
    conn = sqlite3.connect('jogo.db')

    #Cirando um cursor (Ferramenta para mandar executar algum comando)
    cur = conn.cursor()

    #####labels 

    foto = Label(janela1, background=cordefundo, foreground='White' ,text='-----------------\n-                        -\n-                        -\n-                        -\n-  FOTO AQUi  -\n -                         -\n-                         -\n-                         -\n---------------')
    '-----------------\n-                        -\n-                        -\n-                        -\n-  FOTO AQUi  -\n -                         -\n-                         -\n-                         -\n---------------' 
    foto.grid(row=1, column=1 , columnspan=2)

    IDLL = Label(q11, text='ID',background=cordefundo, foreground=cordeletra)
    IDLL.grid( row= 2 ,  column=0 ,sticky=W  )
    nomell=Label(q11, text='Nome', background=cordefundo, foreground=cordeletra)
    nomell.grid(row= 3 ,  column=0 ,sticky=W  )
    TipoLL = Label(q11, text='Tipo', background=cordefundo, foreground=cordeletra)
    TipoLL.grid( row= 4 ,  column= 0 , sticky= W)
    Tipo_de_ataqueLL = Label(q11, text='Tipo de ataque ',background=cordefundo, foreground=cordeletra)
    Tipo_de_ataqueLL.grid( row= 5 ,  column= 0 ,sticky= W)
    habilidade_especialLL = Label(q11, text='Habilidade especial',background=cordefundo, foreground=cordeletra)
    habilidade_especialLL.grid( row= 6 ,  column= 0 ,sticky= W)
    custo_de_estaminaLL = Label(q11, text='Custo de estamina',background=cordefundo, foreground=cordeletra)
    custo_de_estaminaLL.grid( row= 7 ,  column= 0 ,sticky= W )
    pesoLL = Label(q11, text='Peso',background=cordefundo, foreground=cordeletra)
    pesoLL.grid( row= 8 ,  column= 0 ,sticky= W)

    atc_fisicoLL = Label(q2, text='Atc fisico ', background= cordefundo, foreground=cordeletra)
    atc_fisicoLL.grid( row=  1,  column= 1 ,sticky= W) 
    atc_magicoLL = Label(q2, text='Atc magico', background= cordefundo, foreground=cordeletra)
    atc_magicoLL.grid( row=  2,  column= 1 ,sticky= W )
    atc_fogoLL = Label(q2, text='Atc fogo ', background= cordefundo, foreground=cordeletra)
    atc_fogoLL.grid( row= 3 ,  column= 1 ,sticky= W )
    atc_raioLL = Label(q2, text='Atc raio', background= cordefundo, foreground=cordeletra)
    atc_raioLL.grid( row= 4 ,  column= 1  ,sticky= W)
    atc_sagradoLL = Label(q2, text='Atc sagrado ', background= cordefundo, foreground=cordeletra)
    atc_sagradoLL.grid( row= 5 ,  column= 1 ,sticky= W) 
    atc_criticoLL = Label(q2, text='Atc critico  ', background= cordefundo, foreground=cordeletra)
    atc_criticoLL.grid( row= 6 ,  column= 1 ,sticky= W) 

    def_fisicoLL = Label(q3, text='Def fisico', background= cordefundo, foreground=cordeletra)
    def_fisicoLL.grid( row= 1 ,  column= 1 ,sticky= W  ) 
    def_magicoLL = Label(q3, text='Def magico', background= cordefundo, foreground=cordeletra)
    def_magicoLL.grid( row= 2 ,  column= 1 ,sticky= W,)
    def_fogoLL = Label(q3, text='Def fogo', background= cordefundo, foreground=cordeletra)
    def_fogoLL.grid( row= 3 ,  column= 1 ,sticky= W)
    def_raioLL = Label(q3, text='Def raio', background= cordefundo, foreground=cordeletra)
    def_raioLL.grid( row= 4 ,  column= 1 ,sticky= W ) 
    def_sagradoLL = Label(q3, text='Def sagrado', background= cordefundo, foreground=cordeletra)
    def_sagradoLL.grid( row= 5  ,  column= 1 ,sticky= W) 
    def_bonusLL = Label(q3, text='DEF bonus', background= cordefundo, foreground=cordeletra)
    def_bonusLL.grid( row=  6,  column= 1 )

    esc_forcaLL = Label(q4, text='Força', background= cordefundo, foreground=cordeletra)
    esc_forcaLL.grid( row= 1  ,  column= 1 ,sticky= W )
    esc_dexLL = Label(q4, text='Dex', background= cordefundo, foreground=cordeletra)
    esc_dexLL.grid( row= 1 ,  column= 3 ,sticky= W)
    esc_intLL = Label(q4, text='Int', background= cordefundo, foreground=cordeletra)
    esc_intLL.grid( row= 2 ,  column= 1  ,sticky= W)
    esc_feLL = Label(q4, text='Fé', background= cordefundo, foreground=cordeletra)
    esc_feLL.grid( row= 2 ,  column= 3 )
    esc_arcanoLL = Label(q4, text='Arcano ', background= cordefundo, foreground=cordeletra)
    esc_arcanoLL.grid( row= 3 ,  column= 1 ,sticky= W) 

    att_req_forcaLL = Label(q5, text='Força', background= cordefundo, foreground=cordeletra)
    att_req_forcaLL.grid( row= 1 ,  column= 1  ) 
    att_req_dexLL = Label(q5, text='Dex', background= cordefundo, foreground=cordeletra)
    att_req_dexLL.grid( row= 1 ,  column= 3 )
    att_req_intLL = Label(q5, text='Int', background= cordefundo, foreground=cordeletra)
    att_req_intLL.grid( row= 2 ,  column= 1 )
    att_req_feLL = Label(q5, text='Fé', background= cordefundo, foreground=cordeletra)
    att_req_feLL.grid( row= 2 ,  column= 3 )
    att_req_arcanoLL = Label(q5, text='Arcano ', background= cordefundo, foreground=cordeletra)
    att_req_arcanoLL.grid( row= 3 ,  column= 1 ) 

    passeffect  = Label(q6 , text="")
    passeffect.grid(row=1,column=1)

    ###janelas
    ID = Entry(q11,  width= 10 , borderwidth=3,background='grey', foreground='white')
    ID.grid( row= 2, column=1 , sticky= W,)
    nome = Entry(q11 , width=50,borderwidth=1)
    nome.grid( row=3  , column=1 ,sticky=W ,pady=5)

    Tipo = Entry( q11,  width= 20,borderwidth=1)
    Tipo.grid( row= 4, column= 1 ,sticky= W ,pady= 5)
    Tipo_de_ataque  = Entry( q11,  width= 20 ,borderwidth=1)
    Tipo_de_ataque.grid( row= 5, column= 1 ,sticky= W ,columnspan=2,)
    habilidade_especial = Entry( q11,  width= 50,borderwidth=1 )
    habilidade_especial.grid( row= 6, column= 1 ,sticky= W , columnspan=2,pady=5)
    custo_de_estamina = Entry( q11, width= 10 ,borderwidth=1)
    custo_de_estamina.grid( row= 7, column= 1 ,sticky= W,pady= 5)
    peso = Entry( q11,  width= 10,borderwidth=1)
    peso.grid( row= 8, column= 1 ,sticky= W)
    obrigatorio = Label(q11, text=' * Itens obrigatórios *' ,foreground='white', bg=cordefundo)
    obrigatorio.grid(row=8, column=1 ,sticky=E)


    atc_fisico = Entry( q2, width= 10 ,borderwidth=1)
    atc_fisico.grid( row= 1 , column= 2 , sticky= W) 
    atc_magico = Entry( q2, width= 10,borderwidth=1)
    atc_magico.grid( row=2 , column= 2 ,sticky= W)
    atc_fogo = Entry( q2, width= 10,borderwidth=1)
    atc_fogo.grid( row= 3, column= 2 ,sticky= W )
    atc_raio = Entry( q2, width= 10 ,borderwidth=1)
    atc_raio.grid( row= 4 , column=  2,sticky= W)
    atc_sagrado = Entry( q2, width= 10 ,borderwidth=1)
    atc_sagrado.grid( row= 5 , column= 2 ,sticky= W) 
    atc_critico = Entry( q2, width= 10 ,borderwidth=1)
    atc_critico.grid( row= 6 , column= 2 ,sticky= W) 

    def_fisico = Entry( q3, width= 10,borderwidth=1)
    def_fisico.grid( row= 1 , column= 2, padx=10 ) 
    def_magico = Entry( q3, width= 10,borderwidth=1)
    def_magico.grid( row= 2 , column= 2 ,padx=10)
    def_fogo = Entry( q3, width= 10,borderwidth=1)
    def_fogo.grid( row= 3, column= 2 ,padx=10 )
    def_raio = Entry( q3, width= 10 ,borderwidth=1)
    def_raio.grid( row= 4, column= 2 ,padx=10) 
    def_sagrado = Entry( q3, width= 10 ,borderwidth=1)
    def_sagrado.grid( row= 5, column= 2 ,padx=10) 
    def_bonus = Entry(q3, width=10,borderwidth=1)
    def_bonus.grid( row=  6,  column= 2 ,  padx=10)


    esc_forca = Entry( q4, width=10,borderwidth=1)
    esc_forca.grid( row= 1, column= 2  ,sticky= W )
    esc_dex = Entry( q4, width=10,borderwidth=1)
    esc_dex.grid( row= 1, column= 4 ,sticky= W)
    esc_int = Entry( q4, width=10,borderwidth=1)
    esc_int.grid( row= 2, column= 2 ,sticky= W)
    esc_fe = Entry( q4, width=10 ,borderwidth=1)
    esc_fe.grid( row= 2, column= 4 , sticky=W)
    esc_arcano = Entry( q4, width=10,borderwidth=1)
    esc_arcano.grid( row= 3, column= 2 ,sticky= W) 

    att_req_forca = Entry(q5, width=10,borderwidth=1)
    att_req_forca.grid( row= 1, column=2 ,sticky=W ) 
    att_req_dex = Entry( q5,width=10 ,borderwidth=1)
    att_req_dex.grid( row= 1, column= 4 )
    att_req_int = Entry( q5,width=10 ,borderwidth=1)
    att_req_int.grid( row= 2, column= 2 )
    att_req_fe = Entry( q5,width=10 ,borderwidth=1)
    att_req_fe.grid( row= 2, column= 4 )
    att_req_arcano = Entry( q5,width=10 ,borderwidth=1)
    att_req_arcano.grid( row= 3, column= 2 ) 

    passeffect  = Entry(q6, width=50)
    passeffect.grid( row= 1, column= 2 ,sticky=W  )

    but =Button(q7, text="Cadastrar", command= lambda: filtro_vazio() , padx= 50 , borderwidth=3, background='grey')
    but.grid(row=1 , column=1,  )

    but2 =Button(q11, text="Buscar", command= lambda:filtro_Busca() , padx= 50 ,borderwidth=3)
    but2.grid(row=2 , column=1,  )


    ####################
    conn.commit()

    conn.close()


    but3 = Button(janela1, text='SAIR' ,command=lambda: janela1.destroy() ,width=20,background='red' )
    but3.grid(row= 1 , column= 1, sticky=N, pady=(10,0))

    #################----------------------------------------------------########################
    janela1.mainloop()

def vestes():
    return

def itens():
    return

def magias():
    return

def skils():
    return

base = Tk()
base.title('D&D Data Book')
#base.geometry('450x600')

base.overrideredirect(False)
base.geometry('+350+40')

base.resizable(width=False, height=False)
base.iconbitmap('G:/Meu Drive/Códigos/Python/TKinter/D&D/p2.ico')  ### <<< Imagem de icone

fotodofundo = PhotoImage(file='G:/Meu Drive/Códigos/Python/TKinter/D&D/souls22.png')  #### <<<< imagem de fundo
fundo = Canvas(base, width=450, height= 600)
fundo.pack(fill='both', expand=True)
fundo.create_image(0,0, image= fotodofundo , anchor=NW)

bo1 = Button(base, text="Armamento" , command= lambda: armas() ,padx= 30 ,borderwidth=4)
bo1_pack = fundo.create_window( 227,520 , window= bo1, )

bo2 = Button(base, text="Vestes" , command= lambda: vestes() ,padx= 30 ,borderwidth=4,  state= DISABLED)
bo2_pack = fundo.create_window( 100,520 , window= bo2, )

bo3 = Button(base, text="Itens" , command= lambda: itens() ,padx= 30 ,borderwidth=4, state=DISABLED)
bo3_pack = fundo.create_window( 350,520 , window= bo3, )

bo3 = Button(base, text="Skils" , command= lambda: itens() ,padx= 30 ,borderwidth=4, state=DISABLED)
bo3_pack = fundo.create_window( 350,555 , window= bo3, )

bo3 = Button(base, text="Magias" , command= lambda: itens() ,padx= 30 ,borderwidth=4, state=DISABLED)
bo3_pack = fundo.create_window( 100,555 , window= bo3, )


base.mainloop()



