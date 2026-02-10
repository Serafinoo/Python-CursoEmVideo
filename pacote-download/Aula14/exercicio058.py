import random
t = 1
n = 0
r = int(input("Escolha um número entre 0 e 5: "))
while r != n:
    n = random.randint(0,5)
    r = int(input("Você errou, tente novamente: "))
    t += 1
print("Parabéns você acertou!")
print(f"Você acertou em {t} tentativa(s)")
