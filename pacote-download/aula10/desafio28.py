import random
n = random.randint(0,5)
u = int(input("Escolha um número entre 0 e 5: "))
if u == n:
    print("Parabéns você acertou!")
else:
    print(f"""Você errou......
 a resposta era {n}
estou apagando a sua pasta system 32 :)""")