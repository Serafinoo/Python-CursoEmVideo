parar = "N"
numeros = []
valor_cinco = []
while True:
    n = int(input("Digite um número: "))
    numeros.append(n)
    if n == 5:
        valor_cinco.append(1)
    parar = str(input("Você quer continuar? [S/N]")).strip().upper()
    if parar == "N":
        break
numeros.sort(reverse=True)
print(len(numeros))
print(numeros)
if len(valor_cinco) >= 1:
    print(f"O valor 5 foi digitado, e está na lista. ele aparece {len(valor_cinco)} vezes")
else:
    print(f"O valor 5 não foi digitado, e não está na lista")