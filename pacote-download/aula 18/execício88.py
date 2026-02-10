#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai 
# perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para 
# cada jogo, cadastrando tudo em uma lista composta.
from random import randint
jogos = int(input("Quantos jogos você quer que eu sorteie? "))
cadaJogo = []
for _ in range(jogos):
    _ += 1
    cadaJogo.append([randint(0, 60) for n in range(6)])
    print(f"Jogo {_}: {cadaJogo} ")
    cadaJogo.pop()