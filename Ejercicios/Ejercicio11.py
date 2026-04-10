# ============================================
# EJERCICIO: Lista de Compras
# ============================================
# DESCRIPCIÓN:
#   Crea un programa que permita al usuario
#   construir su lista de compras agregando
#   productos uno por uno, y al final muestre
#   el resumen de la lista.
#
# PASOS:
#   1. Crear una lista vacía
#   2. Pedir productos al usuario en un bucle
#   3. Agregar cada producto a la lista
#   4. Detenerse cuando el usuario escriba "listo"
#   5. Mostrar la lista numerada y el total
#
# CONCEPTO CLAVE:
#   - .append() agrega elementos a una lista
#   - len() cuenta cuántos elementos tiene
#   - enumerate() da el índice y valor al recorrer
#     Ejemplo: for i, item in enumerate(lista)
#
# ENTRADA:
#   productos (str) → Nombres de productos
#                     "listo" para terminar
#
# SALIDA ESPERADA:
#   Agrega productos a tu lista (escribe 'listo' para terminar):
#
#   Producto: leche
#   Producto: pan
#   Producto: huevos
#   Producto: listo
#
#   ==============================
#        🛒 LISTA DE COMPRAS
#   ==============================
#    1. leche
#    2. pan
#    3. huevos
#   ------------------------------
#   Total de productos: 3
#   ==============================
#
# PISTAS:
#   - Usa una lista vacía: compras = []
#   - Usa un bucle while True con break
#   - Compara con .lower() por si escribe "Listo" o "LISTO"
#   - Usa enumerate(compras, start=1) para numerar desde 1
# ============================================

# Tu código aquí

compras = []

i = 1
while True:
    lista = input("Ingrese un producto a tu lista =>")
    compras.append(lista)
    confirmacion = input("Has acabado tu lista ? y/n")
    if (confirmacion == "y"):
        print(compras)
        break
