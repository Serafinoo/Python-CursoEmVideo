import datetime
n = 1
cmenor = 0
cmaior = 0
for c in range(1,8):   
    ano = int(input(f"ano de nascimento da {n} pessoa: "))
    n += 1
    if datetime.date.today().year - ano >= 18:
        cmaior += 1
    else:
        cmenor += 1
print(f"""Temos {cmaior} maiores de idade
Temos {cmenor} menores de idade """)