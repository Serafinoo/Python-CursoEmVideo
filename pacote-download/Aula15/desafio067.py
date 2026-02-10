n = 0
c = 0
while True:
    n = int(input("Digite um número para ver a tabuada (numero negativo para parar): "))
    if n < 0:
        break
    for c in range(1, 11):
        print(f"{n} x {c} = {n*c}")
print("programa encerrado")
