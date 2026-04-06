# ============================================
# EJERCICIO: Par o Impar
# ============================================
# DESCRIPCIÓN:
#   Crea un programa que pida al usuario
#   un número y diga si es par o impar.
#   Además que diga si es positivo o negativo.
#
# PASOS:
#   1. Pedir un número al usuario
#   2. Verificar si es par o impar
#   3. Verificar si es positivo, negativo o cero
#   4. Mostrar los resultados
#
# CONCEPTO CLAVE:
#   El operador módulo (%) devuelve el residuo
#   de una división.
#   Ejemplo: 10 % 2 = 0  → par
#            11 % 2 = 1  → impar
#
# ENTRADA:
#   numero (int) → Cualquier número entero
#
# SALIDA ESPERADA:
#   ¿Escribe un número entero? 7
#
#   --------------------------
#   El número 7 es: IMPAR
#   El número 7 es: POSITIVO
#   --------------------------
#
#   ¿Escribe un número entero? -4
#
#   --------------------------
#   El número -4 es: PAR
#   El número -4 es: NEGATIVO
#   --------------------------
#
# PISTAS:
#   - Usa int() para convertir el input
#   - Usa if / elif / else para las condiciones
#   - El operador módulo es %
# ============================================

# Tu código aquí 👇

N = int(input("Ingrese un número: "))

if ((N % 2) == 0 and N > 0):
    print(f"El numero {N} es par y positivo")
elif ((N % 2) == 0 and N < 0):
    print(f"El número {N} es par y negativo")
elif (N > 0):
    print(f"El numero {N} es impar y positivo")
else:
    print(f"El numero {N} es impar y negativo")