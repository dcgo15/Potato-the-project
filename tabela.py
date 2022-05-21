import pandas as pd

dol = pd.Series({"PRODUTO": "Dolar"})
cafe = pd.Series({"PRODUTO": "Café"})
petr = pd.Series({"PRODUTO": "Petroleo"})

tab = pd.DataFrame([dol, cafe, petr])

tab.to_excel("lista_preços2.xlsx", index=False)
