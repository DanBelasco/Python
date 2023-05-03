from tkinter import *
import requests

def pegar_cotacoes():
    
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''
    
    texto2['text'] = texto
    #print(texto)

#pegar_cotacoes()

######################################

janela1 = Tk() ## definção da jenela

janela1.title('Cotação atual das moedas')## defeinição do título de cabeçalho da janela

janela1.geometry('320x220')

texto_orientacao = Label(janela1, text='Clique no botão para ver as cotações')
texto_orientacao.grid(column= 1, row= 1, padx=60 , pady=10) 

botao = Button(janela1, text= 'Consultar', command=pegar_cotacoes ,padx=20, pady=5 )
botao.grid(column= 1, row= 2, padx=10 , pady=10)


texto2 = Label(janela1, text= '' )
texto2.grid(column= 1, row= 3, padx=10 , pady=10)




botao2 = Button(janela1, text= 'Sair', command=exit )
botao2.grid(column= 1, row= 4, padx=10 , pady=10)


janela1.mainloop()## Loop responsavel por manter a janela criada visivel ('travada") 