# ============================================
# EJERCICIO: Tabla de Multiplicar
# ============================================
# DESCRIPCIÓN:
#   Crea un programa que pida un número al
#   usuario y muestre su tabla de multiplicar
#   del 1 al 10.
#
# PASOS:
#   1. Pedir un número al usuario
#   2. Recorrer del 1 al 10 con un bucle
#   3. Mostrar cada multiplicación con su resultado
#
# CONCEPTO CLAVE:
#   - El bucle for recorre una secuencia
#   - range(1, 11) genera números del 1 al 10
#
# ENTRADA:
#   numero (int) → Número del que se genera la tabla
#
# SALIDA ESPERADA:
#   ¿De qué número quieres la tabla? 7
#
#   === Tabla del 7 ===
#   7  x  1  =  7
#   7  x  2  =  14
#   7  x  3  =  21
#   7  x  4  =  28
#   7  x  5  =  35
#   7  x  6  =  42
#   7  x  7  =  49
#   7  x  8  =  56
#   7  x  9  =  63
#   7  x  10 =  70
#
# PISTAS:
#   - Usa int() para convertir el input
#   - Usa for i in range(1, 11) para el bucle
#   - Usa f-strings para formatear la salida
# ============================================

# Tu código aquí 👇
N = int(input("¿De qué número quieres la tabla? "))
if (N <= 10):
    print(f"=====Tabla del {N} =====")
    for i in range(1,11):
        multiplicacion = N * i
        print(f"{N} X {i} = {multiplicacion}")
    print(f"=======================")
else:
    print("El numero no es valido")



