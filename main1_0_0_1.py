from datetime import datetime
import pandas as pd
import requests
import time

lista_preços = []

resposta = requests.get("https://www.commodities-api.com/api/latest?access_key=i2a81wmzhsoa8s6ijq11hg6im4r21197oxf46riux6tcwneckyvt6912mpi3")

preços = resposta.json()

preço_dolar = preços["data"]["rates"]["BRL"]
preço_café = preços["data"]["rates"]["COFFEE"] * 10
preço_petroleo = preços["data"]["rates"]["BRENTOIL"] * 10000

preços_commodities = preço_dolar, preço_café, preço_petroleo
columns = ["Produtos","Preço"]
#index = ["DOLAR", "CAFE", "PETROLEO"]

#print(f"Dolar: {preço_dolar}\nCafe: {preço_café}\nPetroleo: {preço_petroleo}")

lista_preços.append([ preços_commodities])

tabela = pd.DataFrame(preços_commodities,  columns)
tabela.to_excel("lista_preços.xlsx",index=False)

tabela.loc[0, "Preço"] = float(preço_dolar)
tabela.loc[1, "Preço"] = float(preço_café)
tabela.loc[2, "Preço"] = float(preço_petroleo)

tabela.loc[0, "Data atual"] = datetime.now()

print("Preços atualizados:", datetime.now())
print("Previsões futuras: ...(Em Breve)")
