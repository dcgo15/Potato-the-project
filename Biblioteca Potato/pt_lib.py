import requests
import pandas as pd


resposta = requests.get("https://www.commodities-api.com/api/latest?access_key=i2a81wmzhsoa8s6ijq11hg6im4r21197oxf46riux6tcwneckyvt6912mpi3")
preços = resposta.json()
    
coffee = preços["data"]["rates"]["COFFEE"] * 4.6656

tabela = pd.read_excel("lista_preços3.xlsx")
tabela = pd.read_excel("lista_preços3.xlsx")

tabela.loc[0, "PREÇO"] = float(coffee)

tabela.to_excel("lista_preços3.xlsx",index=False)



def café():

    return coffee
