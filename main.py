from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep


browser = webdriver.Chrome()

browser.get("https://www.ifcmarkets.com.br/trading/commodities")
sleep(5)

site = BeautifulSoup(browser.page_source, "html.parser")
print(site.prettify())





#Parte do Codigo html do site IFC markets

'''
<td class="name">
    <a href="/trading-conditions/commodities/copper">
      #C-COPPER
    </a>
</td>

'''
