t1 = int(input("Primeiro termo: "))
r = int(input("Razão: "))
c = 1
p = t1
while c <= 10:
    print(f"{p} ->", end=" ")
    p += r
    c += 1
    if c == 11:
        print("FIM")