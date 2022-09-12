import os
from playwright.sync_api import sync_playwright
import telepot
from secret import cpf
from time import sleep

os.system('playwright install')
bot = telepot.Bot('5641283166:AAEiLUp81ecbOuE28-OEWfntiVLjGVkwbsk')

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    print('-='*20)
    print('BOT INICIADO')
    print('-='*20)
    page.goto('https://ssw.inf.br/2/rastreamento_pf?')
    sleep(5)
    page.locator('//*[@id="cnpjdest"]').fill(cpf)
    page.locator('//*[@id="btn_rastrear"]').click()
    sleep(2)
    while True:
        page.reload()
        info = page.locator('body > div:nth-child(5) > div.table > div:nth-child(3) > table:nth-child(4) > tbody > tr:nth-child(2) > td:nth-child(3) > p:nth-child(2)').text_content()
        bot.sendMessage(1167845071, f'📦O status atual da sua encomenda é:\n\n{info}')
        sleep(14400)