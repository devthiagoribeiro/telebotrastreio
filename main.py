from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import urllib, telepot

print('-='*20)
print('INICIANDO BOT...')
print('-='*20)

navegador = webdriver.Chrome(executable_path='chromedriver.exe')
bot = telepot.Bot('5641283166:AAEiLUp81ecbOuE28-OEWfntiVLjGVkwbsk')

while True:
    print('-='*20)
    print('BOT INICIADO')
    print('-='*20)
    navegador.get('https://ssw.inf.br/2/rastreamento_pf?')
    sleep(5)
    navegador.find_element(By.XPATH, '//*[@id="cnpjdest"]').send_keys('08276822550')
    sleep(2)
    navegador.find_element(By.XPATH, '//*[@id="btn_rastrear"]').click()
    info = navegador.find_element(By.XPATH, '/html/body/div[5]/div[1]/div[3]/table[2]/tbody/tr[2]/td[3]/p[1]').text
    msg = urllib.parse.quote(info)
    numero = '5574999132363'
    print(info)
    bot.sendMessage(1167845071, info)
    sleep(14400)