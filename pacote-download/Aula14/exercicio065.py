resp = "S"
soma = quant = media = 0
while resp == "S":
    numero = int(input("Digite um número: "))
    soma += numero
    quant += 1
    resp = (input("Quer continuar? [S/N]: ")).upper()
media = soma / quant
print(f"Você digitou {quant} números, e a media dos numeros são {media}")
print("FIM")