from math import factorial
n = int(input("Digite um número: "))
c = n
print(f"o fatorial de {n} é: ", end="")
while c > 0:
    print(f" {c} ", end="")
    if c > 1:
        print(" x ", end="")
    else:
        print(f" =  {factorial(n)}",end="")
    c -= 1