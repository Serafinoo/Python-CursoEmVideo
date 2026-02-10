#Crie um programa onde o usuário possa digitar 
# sete valores numéricos e cadastre-os em uma 
# lista única que mantenha separados os valores 
# pares e ímpares. No final, mostre os valores 
# pares e ímpares em ordem crescente.
pares = []
impares = []
numeros = 0
valor = 1
for _ in range(1, 8):
    numeros = int(input(f"Digite o valor número {valor}: "))
    valor += 1
    if numeros % 2 == 0:
        pares.append(numeros)
    else:
        impares.append(numeros)
pares.sort()
impares.sort()
print(f"Os valores pares são: {pares}")
print(f"Os valores ímpares são: {impares}")