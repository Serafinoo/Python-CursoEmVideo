peso = float(input("Digite seu peso: "))
alt = float(input("Digite sua altura: "))
imc = peso/alt**2
print(f"Seu imc é de {imc}")
if imc < 18.5:
    print("Abaixo do peso")
elif imc > 18.5:
    print("Peso ideal")
elif imc > 25:
    print("Sobrepeso")
elif imc > 30:
    print("Obesidade")
elif imc > 40:
    print("Obesidade mórbida")