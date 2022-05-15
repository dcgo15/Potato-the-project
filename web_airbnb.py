import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep


options = Options()
#options.add_argument("--headless")
options.add_argument("window-size=400,800")

browser = webdriver.Chrome(options=options)

browser.get("https://www.airbnb.com")

sleep(3)

input_place = browser.find_element_by_tag_name("input")
input_place.send_keys("Salvador")
input_place.submit()

#site = BeautifulSoup(browser.page_source, "html.parser")
#print(site.prettify())

