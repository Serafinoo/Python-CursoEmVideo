#Crie um programa que gerencie o aproveitamento de 
# um jogador de futebol. O programa vai ler o nome do 
# jogador e quantas partidas ele jogou. Depois vai ler 
# a quantidade de gols feitos em cada partida. No final
# , tudo isso será guardado em um dicionário, incluindo
#  o total de gols feitos durante o campeonato.
i = 0
jogador = {}
jogador["nome"] = str(input("Nome: "))
jogador["partidas"] = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
jogador["gols"] = []
for _ in range (1, jogador["partidas"]+1):
    gols = int(input(f"Quantos gols na partida {_}? "))
    jogador["gols"].append(gols)
jogador["total"] = sum(jogador["gols"])
while True:
    print(jogador)
    for k, v in jogador.items():
        print()
        print(f"{k} tem valor {v}")
    print(f"O jogador {jogador['nome']} jogou {jogador['partidas']} partidas")
    for _ in range(1, jogador["partidas"]+1):
        print(f"Na partida {_}, fez {jogador['gols'][i]}")
        i += 1
    break