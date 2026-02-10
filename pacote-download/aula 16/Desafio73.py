times = "Palmeiras", "Flamengo", "Cruzeiro", "Bragantino", "Ceará", "Bahia", "Fluminense", "Corinthians", "Atlético-MG", "Botafogo", "São Paulo", "Mirassol", "Vasco", "Fortaleza", "Internacional", "Vitória", "Grêmio", "Juventude", "Santos", "Sport"
print(f"Lista de times do Campeonato Brasileiro 2025: {times}")
print(f"Os 5 primeiros times são: {times[0:5]}")
print(f"Os 4 últimos colocados são: {times[16:]}")
print(f"Os Times em ordem alfabética: {sorted(times)}")
print(f"O Sport está na {times.index("Sport")+1} colocação")