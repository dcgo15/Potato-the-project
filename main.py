# Importar 
import requests 
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.cnabrasil.org.br/servicos/precos-commodites"
resposta = requests.get(url)

conteudo = resposta.content

conteudo_site = BeautifulSoup(conteudo , "html.parser")
commodities = conteudo_site.findAll("table", attrs = {"class": "td-nome_produto"})


