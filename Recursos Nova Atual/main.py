'''
import requests

resposta = requests.get("https://www.commodities-api.com/api/latest?access_key=9rzk9chud8q29qw9b6f1hf5ap77s9p81gszwv2pfs0fg6l2yk7xussm6f98p")

preços = resposta.json()


preço_café = preços["data"]["rates"]["COFFEE"] * 4.6656

if preço_café >= 2.0112:
    print("Recomendado: Venda")
else:
    print("Recomendado: Compre")

print(preço_café)
'''

#CLASS APRENDENDO

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def setNome(self, nome):
        self.nome = nome

    def setIdade(self, idade):
        self.idade = idade

    def getNome(self):
        return self.nome

    def getIdade(self):
        return self.idade

persona = Pessoa("Daniel", 16)
print(persona)
