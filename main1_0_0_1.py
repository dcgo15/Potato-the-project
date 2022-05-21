# Criar futuramente uma IA que faça previsoes de preços
# Transformar em uma biblioteca
#adicionar mais produtos

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
