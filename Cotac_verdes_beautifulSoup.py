import pandas as pd
from bs4 import BeautifulSoup
import requests
from datetime import datetime


legumes=[]
produto = 'Tomate - Ceasa'
link = 'https://www.noticiasagricolas.com.br/cotacoes/legumes/tomate-ceasas'
requisicao = requests.get(link)
site = BeautifulSoup(requisicao.text, "html.parser")
tbody = site.find("tbody")
linhas = tbody.find_all("tr")
data = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
for linha in linhas:
    texto_linha = linha.get_text(separator=";")
    lista_textos = texto_linha.split(";")
    nome = lista_textos[1]
    preco = lista_textos[3]
    legumes.append((produto,nome, preco, data))

produto = 'Batata no Atacado'
link = 'https://www.noticiasagricolas.com.br/cotacoes/legumes/batata-ao-produtor-iea'
requisicao = requests.get(link)
site = BeautifulSoup(requisicao.text, "html.parser")
tbody = site.find("tbody")
linhas = tbody.find_all("tr")
data = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
for linha in linhas:
    texto_linha = linha.get_text(separator=";")
    lista_textos = texto_linha.split(";")
    nome = lista_textos[1]
    preco = lista_textos[3]
    legumes.append((produto,nome,preco,data))

produto = 'Batata - Ceasa'
link = 'https://www.noticiasagricolas.com.br/cotacoes/legumes/batata-ceasas'
requisicao = requests.get(link)
site = BeautifulSoup(requisicao.text, "html.parser")
tbody = site.find("tbody")
linhas = tbody.find_all("tr")
data = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
for linha in linhas:
    texto_linha = linha.get_text(separator=";")
    lista_textos = texto_linha.split(";")
    nome = lista_textos[1]
    preco = lista_textos[3]
    legumes.append((produto,nome,preco,data))

produto = 'Cebola no Atacado IEA'
link = 'https://www.noticiasagricolas.com.br/cotacoes/legumes/cebola-no-atacado-iea'
requisicao = requests.get(link)
site = BeautifulSoup(requisicao.text, "html.parser")
tbody = site.find("tbody")
linhas = tbody.find_all("tr")
data = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
for linha in linhas:
    texto_linha = linha.get_text(separator=";")
    lista_textos = texto_linha.split(";")
    nome = lista_textos[1]
    preco = lista_textos[3]
    legumes.append((produto,nome,preco,data))

produto = 'Cebola no Ceasa'
link = 'https://www.noticiasagricolas.com.br/cotacoes/legumes/cebola-no-atacado'
requisicao = requests.get(link)
site = BeautifulSoup(requisicao.text, "html.parser")
tbody = site.find("tbody")
linhas = tbody.find_all("tr")
data = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
for linha in linhas:
    texto_linha = linha.get_text(separator=";")
    lista_textos = texto_linha.split(";")
    nome = lista_textos[1]
    preco = lista_textos[3]
    legumes.append((produto,nome,preco,data))

produto = 'Alface-Ceasa'
link = 'https://www.noticiasagricolas.com.br/cotacoes/verduras/alface-ceasas'
requisicao = requests.get(link)
site = BeautifulSoup(requisicao.text, "html.parser")
tbody = site.find("tbody")
linhas = tbody.find_all("tr")
data = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
for linha in linhas:
    texto_linha = linha.get_text(separator=";")
    lista_textos = texto_linha.split(";")
    nome = lista_textos[1]
    preco = lista_textos[3]
    legumes.append((produto,nome,preco,data))

produto = 'Brocolis-Ceasa'
link = 'https://www.noticiasagricolas.com.br/cotacoes/verduras/brocolos-ceasas'
requisicao = requests.get(link)
site = BeautifulSoup(requisicao.text, "html.parser")
tbody = site.find("tbody")
linhas = tbody.find_all("tr")
data = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
for linha in linhas:
    texto_linha = linha.get_text(separator=";")
    lista_textos = texto_linha.split(";")
    nome = lista_textos[1]
    preco = lista_textos[3]
    legumes.append((produto,nome,preco,data))

produto= 'Couve-Ceasa'
link = 'https://www.noticiasagricolas.com.br/cotacoes/verduras/couve-ceasas'
requisicao = requests.get(link)
site = BeautifulSoup(requisicao.text, "html.parser")
tbody = site.find("tbody")
linhas = tbody.find_all("tr")
data = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
for linha in linhas:
    texto_linha = linha.get_text(separator=";")
    lista_textos = texto_linha.split(";")
    nome = lista_textos[1]
    preco = lista_textos[3]
    legumes.append((produto,nome,preco,data))

produto= 'Repolho-Ceasa'
link = 'https://www.noticiasagricolas.com.br/cotacoes/verduras/repolho-ceasas'
requisicao = requests.get(link)
site = BeautifulSoup(requisicao.text, "html.parser")
tbody = site.find("tbody")
linhas = tbody.find_all("tr")
data = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
for linha in linhas:
    texto_linha = linha.get_text(separator=";")
    lista_textos = texto_linha.split(";")
    nome = lista_textos[1]
    preco = lista_textos[3]
    legumes.append((produto,nome,preco,data))

tabela = pd.DataFrame(legumes,columns=['Cultura','Local','Cotacao','Data'])
tabela.to_excel('cotacao_hj_legumes_hortifruti.xlsx',index=False)