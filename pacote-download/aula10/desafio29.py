km = int(input("Quantos km seu carro percorreu?: "))
m = (km-80)*7
if km < 80:
    print("você não levou multa :)")
else:
    print(f"""MULTADO!
Você excedeu o limite de velocidade
Sua multa vai ser de {m} R$""")