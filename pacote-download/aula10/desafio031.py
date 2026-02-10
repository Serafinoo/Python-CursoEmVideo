km = int(input("Quantos kilometros terá a sua passagem?"))
if km <= 200:
    pas1 = km * 0.50
    print(f"a sua viagem vai custar: {pas1} R$")
else:
    pas2 = km * 0.45
    print(f"A sua viagem vai custar: {pas2} R$")