# Criar futuramente uma IA que faça previsoes de preços
# Transformar em uma biblioteca
#adicionar mais produtos

#Ethanol: 4.666
#NG: 69,52
#brentoil: 12832
#wtioil: 12139
#wheat: 180033
#cotton: 2,045
#coffee: 4,6656
#lumber:  441880
#corn: 61,1370
#rice: 299,6545
#soybean: 287,83
#sugar: 0,0399
#ethanol: 4,666
#cpo: 14341198
#rubber: 298,474

from datetime import datetime
import pandas as pd
import requests
import time

lista_preços = []

resposta = requests.get("https://www.commodities-api.com/api/latest?access_key=i2a81wmzhsoa8s6ijq11hg6im4r21197oxf46riux6tcwneckyvt6912mpi3")

preços = resposta.json()

#Preços

preço_dolar = preços["data"]["rates"]["BRL"]
preço_café = preços["data"]["rates"]["COFFEE"] * 10
preço_petroleo = preços["data"]["rates"]["BRENTOIL"] * 10000

#
'''
#Commodities
preços_commodities = preço_dolar, preço_café, preço_petroleo
#index = ["DOLAR", "CAFE", "PETROLEO"]

#print(f"Dolar: {preço_dolar}\nCafe: {preço_café}\nPetroleo: {preço_petroleo}")

lista_preços.append([preços_commodities])


tabela = pd.DataFrame(preços_commodities, columns = ["Preços"])
'''


tabela = pd.read_excel("lista_preços2.xlsx")


#Preços
tabela.loc[0, "PREÇO"] = float(preço_dolar)
tabela.loc[1, "PREÇO"] = float(preço_café)
tabela.loc[2, "PREÇO"] = float(preço_petroleo)

tabela.loc[0, "DATA ATUAL"] = datetime.now()
tabela.to_excel("lista_preços2.xlsx",index=False)

print(f"---POTATO THE PROJECT---\n***Uma Biblioteca para voce saber o preço real de sua commoditie ppreferida***")
print("Preços atualizados:", datetime.now())
print("Previsões futuras: ...(Em Breve)")
