# Número par o impar
# La entrada sera un número entero y la salida sera un
# mensaje logico donde se indique si el número de entrada es par o impar

N = int(input("Ingresa un número =>"))

if (N % 2 == 0):
    print(f"El numero {N} es par")
else:
    print(f"El numero {N} no es impar")