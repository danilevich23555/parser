import json
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium import webdriver



# def parser_write_html(data):
#
#     with open("myfile.html", "w") as f:
#         f.write(data)
#
# chromedriver = './lib/chromedriver'
# options = webdriver.ChromeOptions()
# options.add_argument("--disable-blink-features=AutomationControlled")
#
#
#
# s = Service(executable_path="./lib/chromedriver")
#
# browser = webdriver.Chrome(options=options, service=s)
#
# browser.get('https://market.yandex.ru/offer/gXBC9f3VsTCE8tua_dKwkA?cpa=1&onstock=1')
# requiredHtml = browser.page_source
# parser_write_html(requiredHtml)
# soup = BeautifulSoup(requiredHtml, features='html.parser')
# table = soup.find(type="application/ld+json")
# # b = json.loads(table.text)



class Parser:

    def parser_writeHTML(URL: str):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        s = Service(executable_path="./lib/chromedriver")
        browser = webdriver.Chrome(options=options, service=s)
        browser.get(URL)
        requiredHtml = browser.page_source
        with open("myfile.html", "a") as f:
            f.write(requiredHtml)




p1 = Parser.parser_writeHTML('https://www.wildberries.ru/catalog/18256273/detail.aspx?targetUrl=MI')
















