#faça um programa que leia nome e peso de várias
#pessoas. guardando tudo em uma lista. no final mostre:
# a) quantas pessoas foram cadastradas
# b) uma listagem com as pessoas mais pesadas (+100 kg)
# c) uma listagem com as mais leves (-70)
galera = list()
pessoas = list()
pesados = list()
leves = list()

while True:
    nome = str(input("Nome: "))
    peso = int(input("Peso: "))

    galera.append([nome, peso])
    
    continuar = str(input("Você quer continuar? [S/N] ")).strip().upper()
    if continuar == "N":
        break

maiorpeso = max(p[1] for p in galera)
menorpeso = min(p[1] for p in galera)

maispesados = [p[0] for p in galera if p[1] == maiorpeso]
maisleves = [p[0] for p in galera if p[1] == menorpeso]
print(f"Você cadastrou ao todo, {len(galera)} pessoas.")
print(f"O maior peso foi de {maiorpeso}. Peso de {maispesados}.")
print(f"O menor peso foi de {menorpeso}. Peso de {maisleves}.")