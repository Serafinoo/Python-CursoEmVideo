# faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final mostre qual foi o menor e o menor valor digitado seguido por suas posições na lista
valores = []
maior = 0
menor = 0
for cont in range(0, 5):
    valores.append(int(input(f"Digite um valor para a posição {cont}: ")))
    if cont == 0:
        maior == menor == valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]
print(f"você digitou os valores {valores}")
print(f"O maior valor é {maior} nas posições", end=" ")
for i, v in enumerate(valores):
    if v == maior:
        print(f"{i}...", end=" ")
print(f"O menor valor é {menor} na posição", end=" ")
for i, v in enumerate(valores):
    if v == menor:
        print(f"{i}...", end=" ")