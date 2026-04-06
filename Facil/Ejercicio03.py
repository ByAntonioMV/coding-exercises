# Tabla de multiplicar
# La entrada sera un número entero y la salida sera la tabla multiplicar del numero entero

N = int(input("Ingrese un numero: "))

if (N <= 10):
    for i in range(1,11):
        multiplicacion = N * i
        print(f"{N} X {i} = {multiplicacion}")
else:
    print("El numero no es valido")