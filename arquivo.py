from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time as tm
import pandas as pd
import win32com.client as win32
import schedule
from datetime import time, timedelta, datetime


def job():
    outlook = win32.Dispatch('outlook.application')

    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico)
    navegador.maximize_window()

    navegador.get('https://economia.uol.com.br/cotacoes/cambio/')
    #time.sleep(3)


    variacao = navegador.find_element(By.XPATH,'/html/body/div[3]/article/div[2]/div/div[1]/div/div/div[1]/div[4]/div/div/div/div[2]/div[1]/div[5]/div/span[2]/span').text
    #variacao = navegador.find_element(By.CLASS_NAME, 'ng-binding').text
    variacao = variacao.replace(",",".")
    variacao = float(variacao)


    if variacao > 1 or variacao < -1:
        mail = outlook.CreateItem(0)
        mail.To = 'brauliocampos0@gmail.com'
        #mail.CC = ''
        #mail.BCC = ''

        mail.Subject = 'Texto teste email'
        mail.Body = '''Valor da variacao do dolar agora é {}'''.format(variacao)

        #attachment = r'pasta\caminho.xlsx'
        #mail.Attachments.Add(attachment)
        mail.Send()



schedule.every(3).minutes.do(job)
while True:
    schedule.run_pending()
    tm.sleep(2)