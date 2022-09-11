from playwright.sync_api import sync_playwright
import telepot
from time import sleep

bot = telepot.Bot('5641283166:AAEiLUp81ecbOuE28-OEWfntiVLjGVkwbsk')

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    while True:
        print('-='*20)
        print('BOT INICIADO')
        print('-='*20)
        page.goto('https://ssw.inf.br/2/rastreamento_pf?')
        sleep(5)
        page.locator('//*[@id="cnpjdest"]').fill('08276822550')
        page.locator('//*[@id="btn_rastrear"]').click()
        sleep(2)
        info = page.locator('body > div:nth-child(5) > div.table > div:nth-child(3) > table:nth-child(4) > tbody > tr:nth-child(2) > td:nth-child(3) > p:nth-child(2)').all_text_contents()
        print(info)
        bot.sendMessage(1167845071, info)
        sleep(14400)