import random
numeros_aleatorios = tuple(random.randint(1, 10) for _ in range(5))
numeros_aleatorios = sorted(numeros_aleatorios)
print(f"O maior é {numeros_aleatorios[4]} e o menor é {numeros_aleatorios[0]}")