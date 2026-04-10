# ============================================
# EJERCICIO: Contador de Vocales
# ============================================
# DESCRIPCIÓN:
#   Crea un programa que pida una palabra o
#   frase al usuario y cuente cuántas vocales
#   tiene en total.
#
# PASOS:
#   1. Pedir una palabra o frase al usuario
#   2. Convertir todo a minúsculas
#   3. Recorrer cada letra
#   4. Contar las vocales
#   5. Mostrar el resultado
#
# CONCEPTO CLAVE:
#   - Puedes recorrer un string letra por letra
#     con un bucle for
#   - El operador in verifica si un elemento
#     está dentro de una lista o string
#     Ejemplo: "a" in "aeiou" → True
#
# ENTRADA:
#   frase (str) → Cualquier palabra o frase
#
# SALIDA ESPERADA:
#   Escribe una palabra o frase: Hola Mundo
#
#   --------------------------
#   Texto:          Hola Mundo
#   Total vocales:  4
#   Vocales found:  o, a, u, o
#   --------------------------
#
#   Escribe una palabra o frase: Ingenieria de Datos
#
#   --------------------------
#   Texto:          Ingenieria de Datos
#   Total vocales:  9
#   Vocales found:  i, e, e, i, e, i, a, e, a, o
#   --------------------------
#
# PISTAS:
#   - Usa .lower() para convertir a minúsculas
#   - Define las vocales como string: "aeiou"
#   - Usa una lista para guardar las vocales encontradas
#   - Usa ", ".join(lista) para imprimir la lista bonito
# ============================================

# Tu código aquí

frase = input("Escribe una palabra o frase: ")

vocales = "aeiouáéíóú"
encontradas = []

for letra in frase.lower():
    if letra in vocales:
        encontradas.append(letra)

print()
print("--------------------------")
print(f"Texto:          {frase}")
print(f"Total vocales:  {len(encontradas)}")
print(f"Vocales found:  {', '.join(encontradas)}")
print("--------------------------")
