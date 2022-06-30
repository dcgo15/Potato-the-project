#BIBLIOTECAS IMPORTADAS
import pandas as pd
import requests
from datetime import datetime

#INICIO
print("------POTATO THE PROJECT------", "\n v1.3.1 - Beta")


link = "https://www.commodities-api.com/api/latest?access_key=9rzk9chud8q29qw9b6f1hf5ap77s9p81gszwv2pfs0fg6l2yk7xussm6f98p"
        
resposta = requests.get(link)
preco = resposta.json()

preço_dolar = preco["data"]["rates"]["BRL"]
café = preco["data"]["rates"]["COFFEE"] * 4.6656
petroleo = preco["data"]["rates"]["BRENTOIL"] * 12832
trigo = preco["data"]["rates"]["WHEAT"] * 180033
algodao = preco["data"]["rates"]["COTTON"] * 2.045
açucar = preco["data"]["rates"]["SUGAR"] * 0.0399
arroz = preco["data"]["rates"]["RICE"] * 299.65
ethanol = preco["data"]["rates"]["ETHANOL"] * 4.666
feijao =preco["data"]["rates"]["SOYBEAN"] * 287.83
ng = preco["data"]["rates"]["NG"] * 69.52
madeira =preco["data"]["rates"]["LUMBER"] * 441.880
borracha = preco["data"]["rates"]["RUBBER"] * 298.474
milho = preco["data"]["rates"]["CORN"] * 61.730
alu = preco["data"]["rates"]["ALU"] * 195.2406
ni = preco["data"]["rates"]["NI"] * 6469.3927
znc = preco["data"]["rates"]["ZNC"] * 12817758.6824
cacau = preco["data"]["rates"]["COCOA"] * 5836185.8190


while True:
    quest = input("Você deseja uma planilha com os preços?[Y / N]:").upper()

    if quest == "Y":
        tabela = pd.read_excel("lista_preços2.xlsx")
        
        tabela.loc[0, "PREÇO"] = float(preço_dolar)
        tabela.loc[1, "PREÇO"] = float(café)
        tabela.loc[2, "PREÇO"] = float(petroleo)
        tabela.loc[3, "PREÇO"] = float(trigo)
        tabela.loc[4, "PREÇO"] = float(algodao)
        tabela.loc[5, "PREÇO"] = float(açucar)
        tabela.loc[6, "PREÇO"] = float(arroz)
        tabela.loc[7, "PREÇO"] = float(ethanol)
        tabela.loc[8, "PREÇO"] = float(feijao)
        tabela.loc[9, "PREÇO"] = float(ng)
        tabela.loc[10, "PREÇO"] = float(madeira)
        tabela.loc[11, "PREÇO"] = float(borracha)
        tabela.loc[12, "PREÇO"] = float(milho)
        tabela.loc[13, "PREÇO"] = float(alu)
        tabela.loc[14, "PREÇO"] = float(ni)
        tabela.loc[15, "PREÇO"] = float(znc)
        tabela.loc[16, "PREÇO"] = float(cacau)

        tabela.loc[0, "DATA ATUAL"] = datetime.now()
        tabela.to_excel("lista_preços2.xlsx", index=False)

        break
        
    elif quest == "N":
        print("Ok, não incomodaremos novamente : )")
        break
    else:
        print("Não entendi : (")

    
#CLASS
class Thepotato:
    def __init__(self):
        pass

    #Nome
    def cafe(self):
        self.cafe = "Café"
        print("O nome da Commoditie é:", self.cafe)
        print("O preço é: USD", café)

        pergunta = input("Deseja ver o preço em R$?[y/n]:")

        if pergunta == "y":
            print("R$",café * preço_dolar)
        elif pergunta == "n":
            print("Ok...")
        else:
            print("Não entendi")

        print("====================")

    def petroleo(self):
        self.petroleo = "Petroleo"
        print("O nome da Commoditie é:", self.petroleo)
        print("O preço é: USD", petroleo)

        pergunta = input("Deseja ver o preço em R$?[y/n]:")

        if pergunta == "y":
            print("R$",petroleo * preço_dolar)
        elif pergunta == "n":
            print("Ok...")
        else:
            print("Não entendi")

        print("====================")


    def tri(self):
        self.tri = "Trigo"
        print("O nome da Commoditie é:", self.tri)
        print("O preço é: USD", trigo)

        pergunta = input("Deseja ver o preço em R$?[y/n]:")

        if pergunta == "y":
            print("R$",trigo * preço_dolar)
        elif pergunta == "n":
            print("Ok...")
        else:
            print("Não entendi")

        print("====================")
        

    def alg(self):
        self.alg = "Algodão"
        print("O nome da Commoditie é:", self.alg)
        print("O preço é: USD", algodao)

        pergunta = input("Deseja ver o preço em R$?[y/n]:")

        if pergunta == "y":
            print("R$",algodao * preço_dolar)
        elif pergunta == "n":
            print("Ok...")
        else:
            print("Não entendi")

        print("====================")

        

    def açu(self):
        self.açu = "Açucar"
        print("O nome da Commoditie é:", self.açu)
        print("O preço é: ", açucar)

        pergunta = input("Deseja ver o preço em R$?[y/n]:")

        if pergunta == "y":
            print("R$",açucar * preço_dolar)
        elif pergunta == "n":
            print("Ok...")
        else:
            print("Não entendi")

        print("====================")
        

    def arro(self):
        self.arro = "Arroz"
        print("O nome da Commoditie é:", self.arro)
        print("O preço é: USD", arroz)

        pergunta = input("Deseja ver o preço em R$?[y/n]:")

        if pergunta == "y":
            print("R$",arroz * preço_dolar)
        elif pergunta == "n":
            print("Ok...")
        else:
            print("Não entendi")

        print("====================")
        

    def eth(self):
        self.eth = "Ethanol"
        print("O nome da Commoditie é:", self.eth)
        print("O preço é: USD", ethanol)

        pergunta = input("Deseja ver o preço em R$?[y/n]:")

        if pergunta == "y":
            print("R$",ethanol * preço_dolar)
        elif pergunta == "n":
            print("Ok...")
        else:
            print("Não entendi")

        print("====================")
        

    def fei(self):
        self.fei = "Feijão"
        print("O nome da Commoditie é:", self.fei)
        print("O preço é: USD", feijao)

        pergunta = input("Deseja ver o preço em R$?[y/n]:")

        if pergunta == "y":
            print("R$",feijao * preço_dolar)
        elif pergunta == "n":
            print("Ok...")
        else:
            print("Não entendi")

        print("====================")
        

    def nat(self):
        self.nat = "Gás Natural"
        print("O nome da Commoditie é:", self.nat)
        print("O preço é: USD", ng)

        pergunta = input("Deseja ver o preço em R$?[y/n]:")

        if pergunta == "y":
            print("R$",ng * preço_dolar)
        elif pergunta == "n":
            print("Ok...")
        else:
            print("Não entendi")

        print("====================")
        

    def mad(self):
        self.mad = "Madeira"
        print("O nome da Commoditie é:", self.mad)
        print("O preço é: USD", madeira)

        pergunta = input("Deseja ver o preço em R$?[y/n]:")

        if pergunta == "y":
            print("R$",madeira * preço_dolar)
        elif pergunta == "n":
            print("Ok...")
        else:
            print("Não entendi")

        print("====================")
        

    def bor(self):
        self.bor = "Borracha"
        print("O nome da Commoditie é:", self.bor)
        print("O preço é: USD", borracha)

        pergunta = input("Deseja ver o preço em R$?[y/n]:")

        if pergunta == "y":
            print("R$",borracha * preço_dolar)
        elif pergunta == "n":
            print("Ok...")
        else:
            print("Não entendi")

        print("====================")
        

    def mil(self):
        self.mil = "Milho"
        print("O nome da Commoditie é:", self.mil)
        print("O preço é: USD", milho)

        pergunta = input("Deseja ver o preço em R$?[y/n]:")

        if pergunta == "y":
            print("R$",milho * preço_dolar)
        elif pergunta == "n":
            print("Ok...")
        else:
            print("Não entendi")

        print("====================")
        

    def alum(self):
        self.alu = "Aluminio"
        print("O nome da Commoditie é:", self.alu)
        print("O preço é: USD", alu)

        pergunta = input("Deseja ver o preço em R$?[y/n]:")

        if pergunta == "y":
            print("R$",alu * preço_dolar)
        elif pergunta == "n":
            print("Ok...")
        else:
            print("Não entendi")

        print("====================")
        

    def niq(self):
        self.ni = "Niquel"
        print("O nome da Commoditie é:", self.ni)
        print("O preço é: USD", ni)

        pergunta = input("Deseja ver o preço em R$?[y/n]:")

        if pergunta == "y":
            print("R$",ni * preço_dolar)
        elif pergunta == "n":
            print("Ok...")
        else:
            print("Não entendi")

        print("====================")
        

    def znco(self):
        self.znc = "Zinco"
        print("O nome da Commoditie é:", self.znc)
        print("O preço é: USD", znc)

        pergunta = input("Deseja ver o preço em R$?[y/n]:")

        if pergunta == "y":
            print("R$",znc * preço_dolar)
        elif pergunta == "n":
            print("Ok...")
        else:
            print("Não entendi")

        print("====================")
        

    def cac(self):
        self.caca = "Cacau"
        print("O nome da Commoditie é:", self.caca)
        print("O preço é: USD", cacau)

        pergunta = input("Deseja ver o preço em R$?[y/n]:")

        if pergunta == "y":
            print("R$",cacau * preço_dolar)
        elif pergunta == "n":
            print("Ok...")
        else:
            print("Não entendi")

        print("====================")


    #Funçao de hora
    def hora(self):
        print("Preços atualizados:", datetime.now())

'''
LEMBRAR DE TIRAR AS CONDIÇÕES DAQUI
TER OPÇÃO PARA REAL
'''

#VARIAVEL DE NOME E PREÇO

commoditie = Thepotato()


commoditie.cafe()
commoditie.tri()
commoditie.hora()


