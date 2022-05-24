import pandas as pd

cafe = pd.Series({"PRODUTO": "Café"})

tab = pd.DataFrame([cafe])

tab.to_excel("lista_preços3.xlsx", index=False)
