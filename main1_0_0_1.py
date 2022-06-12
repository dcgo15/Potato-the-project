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



# Criar futuramente uma IA que faça previsoes de preços
# Transformar em uma biblioteca
#adicionar mais produtos

from datetime import datetime
import pandas as pd
import requests
import time

lista_preços = []

resposta = requests.get("https://www.commodities-api.com/api/latest?access_key=9rzk9chud8q29qw9b6f1hf5ap77s9p81gszwv2pfs0fg6l2yk7xussm6f98p")

preços = resposta.json()

#Preços

preço_dolar = preços["data"]["rates"]["BRL"]
preço_café = preços["data"]["rates"]["COFFEE"] * 4.6656
preço_petroleo = preços["data"]["rates"]["BRENTOIL"] * 12832
tr = preços["data"]["rates"]["WHEAT"] * 180033
alg = preços["data"]["rates"]["COTTON"] * 2.045
açucar = preços["data"]["rates"]["SUGAR"] * 0.0399
arroz = preços["data"]["rates"]["RICE"] * 299.65
eth = preços["data"]["rates"]["ETHANOL"] * 4.666
fei = preços["data"]["rates"]["SOYBEAN"] * 287.83
ng = preços["data"]["rates"]["NG"] * 69.52
lumber = preços["data"]["rates"]["LUMBER"] * 441.880
rubb = preços["data"]["rates"]["RUBBER"] * 298.474
corn = preços["data"]["rates"]["CORN"] * 61.730

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
tabela.loc[3, "PREÇO"] = float(tr)
tabela.loc[4, "PREÇO"] = float(alg)
tabela.loc[5, "PREÇO"] = float(açucar)
tabela.loc[6, "PREÇO"] = float(arroz)
tabela.loc[7, "PREÇO"] = float(eth)
tabela.loc[8, "PREÇO"] = float(fei)
tabela.loc[9, "PREÇO"] = float(ng)
tabela.loc[10, "PREÇO"] = float(lumber)
tabela.loc[11, "PREÇO"] = float(rubb)
tabela.loc[12, "PREÇO"] = float(corn)

tabela.loc[0, "DATA ATUAL"] = datetime.now()
tabela.to_excel("lista_preços2.xlsx",index=False)

print(f"---POTATO THE PROJECT---\n***Uma Biblioteca para voce saber o preço real de sua commoditie ppreferida***")
print("Preços atualizados:", datetime.now())
print("Previsões futuras: ...(Em Breve)")


#VOU CRIAR UMA CLASS
#dolar
print("----COMMODITIES HOJE----","\nConfira os preços aqui:")
nome =print("Dolar:", preço_dolar)
if preço_dolar < preço_dolar * 0.9:
    print("Recomendado: Compra")
else:
    print("Recomendado: Venda")

#cafe
nome =print("Café: ",preço_café)
if preço_café < preço_café * 0.9:
    print("Recomendado: Compra")
else:
    print("Recomendado: Venda")

#petr
nome =print("Petroleo: ",preço_petroleo)
if preço_petroleo < preço_petroleo * 0.9:
    print("Recomendado: Compra")
else:
    print("Recomendado: Venda")

#tri
nome =print("Trigo: ",tr)
if tr < tr * 0.90:
    print("Recomendado: Compra")
else:
    print("Recomendado: Venda")

#alg
nome =print("Algodao", alg)
if alg < alg * 0.90:
    print("Recomendado: Compra")
else:
    print("Recomendado: Venda")

#acucar
nome =print("Açucar:", açucar)
if açucar < açucar * 0.90:
    print("Recomendado: Compra")
else:
    print("Recomendado: Venda")

#arroz
nome =print("Arroz:",arroz)
if arroz < arroz * 0.90:
    print("Recomendado: Compra")
else:
    print("Recomendado: Venda")


#eth
nome =print("Etanol: ",eth)
if eth < eth * 0.90:
    print("Recomendado: Compra")
else:
    print("Recomendado: Venda")

#feijao
nome =print("Feijao:",fei)
if fei < fei * 0.90:
    print("Recomendado: Compra")
else:
    print("Recomendado: Venda")

#ng
nome =print("Gas Natural: ",ng)
if ng < ng * 0.90:
    print("Recomendado: Compra")
else:
    print("Recomendado: Venda")

#lumber
nome =print("Madeira: ",lumber)
if lumber < lumber * 0.90:
    print("Recomendado: Compra")
else:
    print("Recomendado: Venda")

#rubb
nome =print("Borracha:",rubb)
if rubb < rubb * 0.90:
    print("Recomendado: Compra")
else:
    print("Recomendado: Venda")

#corn
nome = print("Milho:",corn)
if corn < corn * 0.90:
    print("Recomendado: Compra")
else:
    print("Recomendado: Venda")


