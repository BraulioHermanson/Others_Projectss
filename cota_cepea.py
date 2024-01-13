from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.maximize_window()

navegador.get('https://www.cepea.esalq.usp.br/br/indicador/milho.aspx')
table_element = navegador.find_element(By.XPATH,'//*[@id="imagenet-content"]/div[2]/div[2]/div[1]/div[2]/div[1]').text
tabela = table_element.split()

df = pd.DataFrame(tabela)
time.sleep(5)
navegador.quit()
cabecalho = df[0:6].T

cabecalho.rename(columns={0:'DATA',
                          1:'VALOR R$*',
                          2:'VAR./DIA',
                          3:'VAR./MÊS',
                          4:'VALOR US$*'},inplace=True)

cabecalho.drop(labels=[5],axis=1,inplace=True)

linha_dia = df[6:11].T

linha_dia.columns = cabecalho.columns

# Para ter a primeira linha preenchida e disso populando a base
# linha_dia.to_excel('milhos.xlsx',index=False)

base = pd.read_excel('milhos.xlsx')
base_add = pd.concat([base,linha_dia])
base_add.drop_duplicates(inplace=True)
base_add.to_excel('milhos.xlsx',index=False)