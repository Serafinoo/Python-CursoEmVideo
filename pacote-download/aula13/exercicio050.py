a1 = int(input("Primeiro termo: "))
r = int(input("Razão: "))
for p in range(a1, 30, r):
    print(p, end=" ")
    p += r