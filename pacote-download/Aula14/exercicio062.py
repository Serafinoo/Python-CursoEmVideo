t1 = int(input("Primeiro termo: "))
r = int(input("Razão: "))
c = 1
p = t1
total = 0
resp = 10
while resp != 0:
    total = total + resp
    while c <= total:
        print(f"{p} ->", end=" ")
        p += r
        c += 1
    print("PAUSA")
    resp = int(input("Quantos termos você quer adicionar?: "))
print("FIM")