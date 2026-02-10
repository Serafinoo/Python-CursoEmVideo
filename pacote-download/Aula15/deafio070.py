total_gasto = 0
maior_mil = 0
barato = " "
menor = 0
cont = 0
while True:
    nome_produto = input("Digite o nome do produto: ")
    preco_produto = int(input("Digite o preço do produto: "))
    cont += 1 
    if cont == 1 or preco_produto < menor:
        menor = preco_produto
        barato = nome_produto
    total_gasto += preco_produto
    if preco_produto >= 1000:
        maior_mil += 1
    continuar = input("Você quer continuar? [S/N]: ").strip().upper()[0]
    if continuar == "N":
        break
print(f"O total gasto foi de {total_gasto}")
print(f"Você comprou {maior_mil} produtos com mais de mil reais")
print(f"O produto mais barato foi {barato}")
print("Fim do programa")