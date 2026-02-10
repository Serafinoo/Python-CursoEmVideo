#Crie um programa que leia nome, ano de nascimento e 
# carteira de trabalho e cadastre-o (com idade) em um 
# dicionário. Se por acaso a CTPS for diferente de ZERO
# , o dicionário receberá também o ano de contratação 
# e o salário. Calcule e acrescente, além da idade, com
#  quantos anos a pessoa vai se aposentar.
from datetime import datetime
trabalhador = {}
while True:
    trabalhador["nome"] = str(input("Digite seu nome: "))
    nasc = int(input("Ano de nascimento: "))
    trabalhador["idade"] = datetime.now().year - nasc
    trabalhador["ctps"] = int(input("Carteira de trabalho (0 = não tem): "))
    if trabalhador["ctps"] == 0:
        for k, v in trabalhador.items():
            print("")
            print(f"{k} tem valor {v}")
        break
    trabalhador["anoContrat"] = int(input("Ano de contratação: "))
    trabalhador["aposentadoria"] = trabalhador["idade"] + ((trabalhador["anoContrat"] + 35) - datetime.now().year)
    trabalhador["salario"] = float(input("Salário: R$"))
    for k, v in trabalhador.items():
        print("")
        print(f"{k} tem valor {v}")
    break