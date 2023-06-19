#https://docs.awesomeapi.com.br/api-de-moedas
#https://economia.awesomeapi.com.br/json/all
import tkinter as tk
from tkinter import ttk #combobox
from tkcalendar import DateEntry
import requests
from tkinter.filedialog import askopenfilename
import pandas as pd
from datetime import datetime
import numpy as np

requisicao = requests.get('https://economia.awesomeapi.com.br/json/all')
dicionario_moedas = requisicao.json()

lista_moedas = list(dicionario_moedas.keys())

def pegar_cotacao():
    moeda = combobox_selecionarmoeda.get()
    data_cotacao = calendario_moeda.get()
    ano = data_cotacao[-4:]
    mes = data_cotacao[3:5]
    dia = data_cotacao[:2]
    link = f'https://economia.awesomeapi.com.br/{moeda}/10?start_date={ano}{mes}{dia}&end_date={ano}{mes}{dia}'
    requisicao_moeda = requests.get(link)
    cotacao = requisicao_moeda.json()
    try:
        valor_moeda = cotacao[0]['bid']
        label_textocotacao['text'] = f"A cotacao da {moeda} no dia {dia}/{mes}/{ano} foi de: R$ {valor_moeda}"
    except:
        valor_moeda = 0
        label_textocotacao['text'] = f"A cotacao da {moeda} no dia {dia}/{mes}/{ano} foi de: R$ {valor_moeda}"

def selecionar_arquivo():
    caminho_arquivo = askopenfilename(title="Selecione o Arquivo de Moeda")
    var_caminhoarquivo.set(caminho_arquivo)
    if caminho_arquivo:
        label_arquivoselecionado['text'] = f"Arquivo selecionado: {caminho_arquivo[65:]}"

def atualizar_cotacoes():
    try:
        # ler o dataframe de moedas
        df = pd.read_excel(var_caminhoarquivo.get())
        moedas = df.iloc[:, 0]
        # pegar a data de inicio e data de fim das cotacoes
        data_inicial = calendario_datainicial.get()
        data_final = calendario_datafinal.get()
        ano_inicial = data_inicial[-4:]
        mes_inicial = data_inicial[3:5]
        dia_inicial = data_inicial[:2]

        ano_final = data_final[-4:]
        mes_final = data_final[3:5]
        dia_final = data_final[:2]

        for moeda in moedas:
            link = f"https://economia.awesomeapi.com.br/json/daily/{moeda}-BRL/?" \
                   f"start_date={ano_inicial}{mes_inicial}{dia_inicial}&" \
                   f"end_date={ano_final}{mes_final}{dia_final}"

            requisicao_moeda = requests.get(link)
            cotacoes = requisicao_moeda.json()
            for cotacao in cotacoes:
                timestamp = int(cotacao['timestamp'])
                bid = float(cotacao['bid'])
                data = datetime.fromtimestamp(timestamp)
                data = data.strftime('%d/%m/%Y')
                if data not in df:
                    df[data] = np.nan

                df.loc[df.iloc[:, 0] == moeda, data] = bid
        df.to_excel("Teste.xlsx")
        label_atualizarcotacoes['text'] = "Arquivo Atualizado com Sucesso"
    except:
        label_atualizarcotacoes['text'] = "Selecione um arquivo Excel no Formato Correto"

janela = tk.Tk()
janela.title("Ferramenta de Cotação de Moedas")

label_cotacaomoeda = tk.Label(text = "Cotação de 1 moeda especial",borderwidth=2, relief="solid")
label_cotacaomoeda.grid(row=0, column =0, padx=10,pady=10, sticky ="nswe",columnspan=3)


label_selecionarmoeda = tk.Label(text = "Selecionar Moeda",anchor='e')
label_selecionarmoeda.grid(row=1, column =0, padx=10,pady=10, sticky ="nswe",columnspan=2)
combobox_selecionarmoeda = ttk.Combobox(values=lista_moedas)
combobox_selecionarmoeda.grid(row=1,column=2,padx=10,pady=10,sticky="nswe")


label_selecionardata = tk.Label(text = "Selecionar o dia que deseja pegar a cotação",anchor='e')
label_selecionardata.grid(row=2, column =0, padx=10,pady=10, sticky ="nswe",columnspan=2)
calendario_moeda = DateEntry(year=2023,locale = 'pt_br')
calendario_moeda.grid(row=2, column=2, padx=10,pady=10, sticky= "nswe")

label_textocotacao = tk.Label(text="")
label_textocotacao.grid(row=3, column=0, padx=10,pady=10, sticky= "nswe",columnspan= 2)
botao_pegarcotacao = tk.Button(text="Pegar Cotação", command=pegar_cotacao)
botao_pegarcotacao.grid(row=3, column=2, padx=10, pady=10, sticky="nswe")


#Cotaçao de varias moedas
label_cotacaovariasmoeda = tk.Label(text = "Cotação de Multiplas Moedas",borderwidth=2, relief="solid")
label_cotacaovariasmoeda.grid(row=4, column =0, padx=10,pady=10, sticky ="nswe",columnspan=3)

label_selecionararquivo = tk.Label(text='Selecione um arquivo em excel com as moedas na coluna A')
label_selecionararquivo.grid(row=5, column=0, padx=10, pady =10, sticky="nswe",columnspan=2)
botao_selecionararquivo = tk.Button(text="Clique para Selecionar",command = selecionar_arquivo)
botao_selecionararquivo.grid(row=5, column=2, padx=10, pady= 10, sticky="nswe")

label_arquivoselecionado = tk.Label(text="Nenhum arquivo selecionado",anchor='e')
label_arquivoselecionado.grid(row=6, column=0, columnspan=3, padx=10,pady=10,sticky="nswe")

var_caminhoarquivo = tk.StringVar()

label_datainicial= tk.Label(text = "Data incial",anchor='e')
label_datainicial.grid(row=7,column=0, padx=10, pady=10, sticky="nswe",columnspan=2)
calendario_datainicial = DateEntry(year=2023, locale='pt_br')
calendario_datainicial.grid(row=7, column=2,padx=10, pady= 10, sticky="nswe" )

label_datafinal = tk.Label(text = "Data final",anchor='e')
label_datafinal.grid(row=8,column=0, padx=10, pady=10, sticky="nswe",columnspan=2)
calendario_datafinal = DateEntry(year=2023, locale='pt_br')
calendario_datafinal.grid(row=8, column=2,padx=10, pady= 10, sticky="nswe" )

botao_atualizarcotacoes = tk.Button(text='Atualizar cotações', command=atualizar_cotacoes)
botao_atualizarcotacoes.grid(row=9, column=0, padx=10, pady=10, stick='nswe')

label_atualizarcotacoes = tk.Label(text="")
label_atualizarcotacoes.grid(row=9, column=1,padx=10, pady= 10, sticky="nswe",columnspan=2 )

botao_fechar = tk.Button(text="Fechar",command = janela.quit)
botao_fechar.grid(row=10, column=2,padx=10, pady= 10, sticky="nswe")


janela.mainloop()