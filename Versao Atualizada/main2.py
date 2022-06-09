import pandas as pd
import requests


print("---POTATO THE PROJECT---", "\n Versão 1.3.1 - Beta")


link = "https://www.commodities-api.com/api/latest?access_key=9rzk9chud8q29qw9b6f1hf5ap77s9p81gszwv2pfs0fg6l2yk7xussm6f98p"
        
resposta = requests.get(link)
preco = resposta.json()

café = preco["data"]["rates"]["COFFEE"] * 4.6656


class Commodities:
    def __init__(self, nome):
        self.nome = nome

    def name(self):
        print("Nome da commoditie: ", self.nome)

    def preços(self):
        print("O preço é: ", café)


commo = Commodities("cafe")
commo.name()

preco = Commodities("cafe")
preco.preços()

