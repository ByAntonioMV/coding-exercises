# ============================================
# EJERCICIO: Conversor de Temperaturas
# ============================================
# DESCRIPCIÓN:
#   Crea un programa que convierta una temperatura
#   de Celsius a Fahrenheit y a Kelvin.
#
# PASOS:
#   1. Pedir la temperatura en Celsius
#   2. Convertir a Fahrenheit
#   3. Convertir a Kelvin
#   4. Mostrar los tres resultados
#
# FÓRMULAS:
#   Fahrenheit = (Celsius * 9/5) + 32
#   Kelvin     = Celsius + 273.15
#
# ENTRADA:
#   temperatura (float) → Temperatura en grados Celsius
#
# SALIDA ESPERADA:
#   ¿Cuál es la temperatura en Celsius? 100
#
#   --------------------------
#   Celsius:    100.00 °C
#   Fahrenheit: 212.00 °F
#   Kelvin:     373.15 °K
#   --------------------------
#
# PISTAS:
#   - Usa input() para pedir la temperatura
#   - Convierte a número con float()
#   - Usa round(numero, 2) para redondear
#   - Para imprimir usa print() con f-strings:
#     Ejemplo: print(f"Resultado: {variable}")
# ============================================

# Tu código aquí 👇

celsius = float(input("Ingresa tu temperatura en celcius: "))
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print("***********************")
print("El resultado en las diferentes temperaturas es:")
print(f"Celciuss: {celsius}")
print(f"Fahrenheit: {fahrenheit}")
print(f"Kelvin: {kelvin}")
print("***********************")