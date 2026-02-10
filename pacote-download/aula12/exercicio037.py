import binascii
n = int(input("Digite um número: "))
b = str(input("Escolha uma base numérica Binario(bin), octal(oct), hexadecimal(hex): "))
if b == "bin":
        print(f"Em binário seria: {bin(n)[2:]}")
elif b == "oct":
        print(f"Em octal seria: {oct(n)[2:]}")
elif b == "hex":
        print(f"Em hexadecimal seria: {hex(n)[2:]}")