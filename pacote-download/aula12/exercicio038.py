n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
igual = bool(n1==n2)
if n1 > n2:
    print("O primeiro valor é maior")
elif n1 < n2:
    print("O segundo valor é maior")
elif igual == True:
    print("Os números são iguais")
