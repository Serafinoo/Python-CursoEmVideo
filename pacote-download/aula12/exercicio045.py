import random
pedra = "pedra"
papel = "papel"
tesoura = "tesoura"
lista = [pedra, papel, tesoura]
mac = random.choice(lista)
usu = int(input("""Escolha entre
    [1] Pedra
    [2] Papel
    [3] Tesoura
                Escolha: """)) 
print(f"A maquina escolheu {mac}")
if usu == 1 and mac == pedra or usu == 2 and mac == papel or usu == 3 and mac == tesoura:
    print("EMPATE")
elif usu == 1 and mac == papel or usu == 2 and mac == tesoura or usu == 3 and mac == pedra:
    print("MAQUINA VENÇEU")
elif usu == 1 and mac == tesoura or usu == 2 and mac == pedra or usu == 3 and mac == papel:
    print("VOCÊ VENCEU")