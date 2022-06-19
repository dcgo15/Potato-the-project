import pandas as pd

dol = pd.Series({"PRODUTO": "Dolar/BRL"})
cafe = pd.Series({"PRODUTO": "Café/Kg"})
petr = pd.Series({"PRODUTO": "Petroleo"})
tr = pd.Series({"PRODUTO": "Trigo"})
alg = pd.Series({"PRODUTO": "Algodão"})
açucar = pd.Series({"PRODUTO": "Açucar"})
arroz = pd.Series({"PRODUTO": "Arroz"})
eth = pd.Series({"PRODUTO": "Etanol"})
fei = pd.Series({"PRODUTO": "Feijao"})
ng = pd.Series({"PRODUTO": "Gas Natural"})
lumber = pd.Series({"PRODUTO": "Madeira"})
rubb = pd.Series({"PRODUTO": "Borracha"})
corn = pd.Series({"PRODUTO": "Milho"})

#NOVOS COMMODITIES
alu = pd.Series({"PRODUTO": "Aluminio"})
ni = pd.Series({"PRODUTO": "Niquel"})
znc = pd.Series({"PRODUTO": "Zinco"})
tin = pd.Series({"PRODUTO": "Titanio"})
cac = pd.Series({"PRODUTO": "Cacau"})

tab = pd.DataFrame([dol, cafe, petr, tr, alg, açucar, arroz, eth, fei,
                    ng, lumber, rubb, corn, alu, ni, znc, tin, cac])

tab.to_excel("lista_preços2.xlsx", index=False)
