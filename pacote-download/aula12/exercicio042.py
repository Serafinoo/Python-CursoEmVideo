r1 = float(input("Digite o comprimento de uma reta: "))
r2 = float(input("Digite o comprimento de uma reta: "))
r3 = float(input("Digite o comprimento de uma reta: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Isso pode ser um triangulo")
else:
    print("Isso não pode ser um triangulo")
if r1 == r2 == r3:
    print("Esse triangulo é equilatero")
elif r1 != r2 != r3 != r1:
    print("Esse triangulo é escaleno")
else:
    print("Esse triangulo é isósceles")