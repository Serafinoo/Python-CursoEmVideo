tot18 = 0
M = 0
F = 0
while True:
    idade = int(input("Idade: "))
    if idade >= 18:
        tot18 += 1
    sexo = input("Sexo[M/F]: ").strip().upper()[0]
    if sexo == "M":
        M += 1
    elif sexo == "F" and idade >= 20:
        F += 1
    continua = input("Você quer continuar? [S/N]: ").strip().upper()[0]
    if continua == "N":
        break
print(f"O total de pessoas com mais de 18 anos são {tot18}")
print(f"O total de homens são {M}")
print(f"Tem {F} mulheres com mais de 20 anos ")