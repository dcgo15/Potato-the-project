#BIBLIOTECAS IMPORTADAS
import pandas as pd
import requests
from datetime import datetime
import time

#INICIO
print("---POTATO THE PROJECT---", "\n Versão 1.3.1 - Beta")


link = "https://www.commodities-api.com/api/latest?access_key=9rzk9chud8q29qw9b6f1hf5ap77s9p81gszwv2pfs0fg6l2yk7xussm6f98p"
        
resposta = requests.get(link)
preco = resposta.json()

café = preco["data"]["rates"]["COFFEE"] * 4.6656

#CLASS
class Commodities:
    def __init__(self):
        pass

    def cafe(self):
        self.cafe = "café"
        print("O nome da Commoditie é:", self.cafe)
        print("O preço é: ", café)

    def hora(self):
        print("Preços atualizados:", datetime.now())
        

#VARIAVEL DE NOME E PREÇO
        
commoditie = Commodities()

commoditie.cafe()
commoditie.hora()
 

