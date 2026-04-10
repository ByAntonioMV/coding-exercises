# Mayor de tres
# La entrada seran 3 numeros y la salida sera el numero N mayor

N1 = int(input("Ingresa el primer número: "))
N2 = int(input("Ingresa el segundo número: "))
N3 = int(input("Ingresa el tercer número: "))

if (N1 > N2 and N1 > N3):
    print(f"{N1} es el mayor")
if (N2 > N1 and N2 > N3):
    print(f"{N2} es el mayor")
if (N3 > N1 and N3 > N2):
    print(f"{N3} es el mayor")