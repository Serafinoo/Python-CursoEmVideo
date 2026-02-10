numeros = []
par = []
impar = []
n = 0
continuar = "S"
while True:
    n = int(input(f"Digite um número: "))
    numeros.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    continuar = str(input("Você deseja continuar? [S/N]: ")).strip().upper()
    if continuar == "N":
        break
print(numeros)
print(par)
print(impar)