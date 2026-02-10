numeros = tuple(int(input("Digite 1 número: ")) for _ in range (4))
print(f"Você digitou os valores {numeros}")
print(f"O número 9 apareceu {numeros.count(9)} vezes")
if 3 in numeros:
    print(f"O número 3 apareceu pela primeira vez ns {numeros.index(3)+1}ª colocação")
else:
    print("3 não foi digitado")
print(f"Os pares digitados foram: ", end="")
for n in numeros:
    if n % 2 == 0:
        print(n, end=" ")