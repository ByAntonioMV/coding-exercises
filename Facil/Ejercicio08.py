# ============================================
# EJERCICIO: Adivina el Número
# ============================================
# DESCRIPCIÓN:
#   Crea un programa que genere un número
#   aleatorio del 1 al 10 y el usuario tenga
#   que adivinarlo en máximo 3 intentos.
#
# PASOS:
#   1. Generar un número aleatorio del 1 al 10
#   2. Pedir al usuario que adivine el número
#   3. Indicar si el número es mayor o menor
#   4. Repetir hasta 3 intentos
#   5. Mostrar si ganó o perdió
#
# CONCEPTO CLAVE:
#   - random.randint(1, 10) genera un número
#     aleatorio entre 1 y 10
#   - Los bucles while repiten código
#     mientras una condición sea verdadera
#
# ENTRADA:
#   intento (int) → Número que adivina el usuario
#
# SALIDA ESPERADA:
#   === Adivina el Número ===
#   Tengo un número del 1 al 10, tienes 3 intentos.
#
#   Intento 1 de 3 → ¿Cuál es el número? 5
#   Demasiado bajo, intenta de nuevo.
#
#   Intento 2 de 3 → ¿Cuál es el número? 8
#   Demasiado alto, intenta de nuevo.
#
#   Intento 3 de 3 → ¿Cuál es el número? 7
#   🎉 ¡Correcto! Adivinaste en 3 intentos.
#
#   --- Si pierde ---
#   ❌ ¡Perdiste! El número era 7.
#
# PISTAS:
#   - Importa random al inicio: import random
#   - Usa while para el bucle de intentos
#   - Usa un contador para llevar los intentos
#   - Usa break para salir del bucle si adivina
# ============================================

# Tu código aquí 👇