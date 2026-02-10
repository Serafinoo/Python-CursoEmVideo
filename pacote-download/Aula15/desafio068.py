import random

while True:
    jogador = int(input("Digite um número: "))
    maquina = random.randint(1, 11)
    total = jogador + maquina
    tipo = " "
    while tipo not in "PpTi":
        tipo = str(input("Par ou impar [P/I]: "))
    print(f"Você jogou o número {jogador} e a maquina jogou {maquina} o total é de {total}")
    if tipo == "P" and "p":
        if total % 2 == 0:
            print("Você venceu!")
            v += 1
        else:
            print("Você perdeu")
            break
    elif tipo == "I" and "i":
        if total % 2 == 0:
            print("Você venceu!")
            v += 1
        else:
            print("Você perdeu")
            break