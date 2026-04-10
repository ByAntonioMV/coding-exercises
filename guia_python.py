# ============================================================
#         GUÍA DE REFERENCIA RÁPIDA - PYTHON
#         Autor: Tu guía personal de Python 🐍
# ============================================================
# Propósito: Consulta este archivo cuando tengas dudas sobre
#            la sintaxis o uso de los conceptos básicos de Python.
# Contenido:
#   1. Variables y Tipos de Datos
#   2. Operadores
#   3. Strings (Cadenas de texto)
#   4. Condicionales (if / elif / else)
#   5. Bucles (while / for)
#   6. Arreglos (Listas)
#   7. Funciones
#   8. Diccionarios
#   9. Manejo de errores (try / except)
# ============================================================


# ============================================================
# 1. VARIABLES Y TIPOS DE DATOS
# ============================================================
# Una variable es un espacio en memoria donde guardamos datos.
# No necesitas declarar el tipo, Python lo detecta solo.

nombre = "Ana"          # str  → texto (string)
edad = 25               # int  → número entero
altura = 1.65           # float → número decimal
activo = True           # bool → True o False

# Para ver el tipo de una variable:
# print(type(nombre))   → <class 'str'>

# Imprimir variables
print(nombre)           # Ana
print(edad)             # 25
print(type(altura))     # <class 'float'>

# Convertir tipos (casting)
numero_texto = "10"
numero_entero = int(numero_texto)    # "10" → 10
numero_decimal = float(numero_texto) # "10" → 10.0
texto_numero = str(25)               # 25   → "25"


# ============================================================
# 2. OPERADORES
# ============================================================

# Aritméticos
suma        = 5 + 3     # 8
resta       = 5 - 3     # 2
multiplicar = 5 * 3     # 15
dividir     = 5 / 3     # 1.666... (siempre da float)
div_entera  = 5 // 3    # 1   (división entera)
modulo      = 5 % 3     # 2   (residuo de la división)
potencia    = 5 ** 2    # 25

# Comparación (devuelven True o False)
igual       = 5 == 5    # True
diferente   = 5 != 3    # True
mayor       = 5 > 3     # True
menor       = 5 < 3     # False
mayor_igual = 5 >= 5    # True

# Lógicos
and_op = True and False  # False (ambos deben ser True)
or_op  = True or False   # True  (al menos uno es True)
not_op = not True        # False (invierte el valor)


# ============================================================
# 3. STRINGS (CADENAS DE TEXTO)
# ============================================================

saludo = "Hola, Mundo"

# Métodos útiles de strings
print(saludo.upper())       # HOLA, MUNDO
print(saludo.lower())       # hola, mundo
print(saludo.replace("Mundo", "Python"))  # Hola, Python
print(len(saludo))          # 11 (cantidad de caracteres)
print(saludo[0])            # H  (primer carácter, índice 0)
print(saludo[-1])           # o  (último carácter)
print(saludo[0:4])          # Hola (slicing: del índice 0 al 3)

# Verificar contenido
print("Hola" in saludo)     # True
print(saludo.startswith("Hola"))  # True
print(saludo.endswith("Mundo"))   # True

# Formateo de strings (f-strings) → la forma más moderna
nombre = "Carlos"
anio = 2024
print(f"Hola, {nombre}! Estamos en {anio}.")
# → Hola, Carlos! Estamos en 2024.

# strip() elimina espacios al inicio y al final
texto = "   hola   "
print(texto.strip())        # "hola"

# split() divide un string en una lista
frase = "manzana,pera,uva"
frutas = frase.split(",")   # ["manzana", "pera", "uva"]

# join() une una lista en un string
unido = ", ".join(frutas)   # "manzana, pera, uva"


# ============================================================
# 4. CONDICIONALES (if / elif / else)
# ============================================================
# Permiten ejecutar código según una condición.
# Sintaxis:
#   if condicion:
#       código si es True
#   elif otra_condicion:
#       código si la segunda es True
#   else:
#       código si ninguna fue True

nota = 85

if nota >= 90:
    print("Excelente")
elif nota >= 70:
    print("Aprobado")       # ← Se ejecuta este
elif nota >= 60:
    print("Suficiente")
else:
    print("Reprobado")

# Condicional en una línea (ternario)
estado = "Mayor" if edad >= 18 else "Menor"
print(estado)               # Mayor


# ============================================================
# 5. BUCLES
# ============================================================

# ---------------------------
# 5.1 Bucle WHILE
# ---------------------------
# Se repite MIENTRAS la condición sea True.
# Útil cuando no sabes cuántas veces se va a repetir.

contador = 1
while contador <= 5:
    print(f"Vuelta {contador}")
    contador += 1           # Importante: actualizar para no ciclo infinito

# while con break (salir del bucle antes)
numero = 0
while True:
    numero += 1
    if numero == 3:
        break               # Sale del bucle cuando número es 3

# ---------------------------
# 5.2 Bucle FOR
# ---------------------------
# Recorre una secuencia (lista, string, range).
# Útil cuando sabes cuántas veces se va a repetir.

# Recorrer un rango de números
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):       # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):   # 0, 2, 4, 6, 8 (de 2 en 2)
    print(i)

# Recorrer un string
for letra in "Python":
    print(letra)            # P, y, t, h, o, n

# continue → salta a la siguiente vuelta sin ejecutar el resto
for i in range(5):
    if i == 2:
        continue            # Salta cuando i es 2
    print(i)                # Imprime: 0, 1, 3, 4


# ============================================================
# 6. ARREGLOS (LISTAS)
# ============================================================
# Una lista puede guardar varios valores en una sola variable.
# Los índices empiezan en 0.
# Se puede mezclar tipos, pero no es recomendable.

frutas = ["manzana", "pera", "uva", "naranja"]

# Acceder a elementos
print(frutas[0])            # manzana (primer elemento)
print(frutas[-1])           # naranja (último elemento)
print(frutas[1:3])          # ["pera", "uva"] (slicing)

# Métodos principales
frutas.append("fresa")      # Agrega al final
frutas.insert(1, "mango")   # Inserta en posición 1
frutas.remove("pera")       # Elimina por valor
frutas.pop()                # Elimina el último elemento
frutas.pop(0)               # Elimina por índice
frutas.sort()               # Ordena alfabéticamente
frutas.reverse()            # Invierte el orden
print(len(frutas))          # Cantidad de elementos
print("uva" in frutas)      # True si "uva" está en la lista

# Recorrer una lista con for
for fruta in frutas:
    print(fruta)

# Recorrer con índice usando enumerate()
for i, fruta in enumerate(frutas, start=1):
    print(f"{i}. {fruta}")

# Listas de números
numeros = [5, 2, 8, 1, 9]
print(min(numeros))         # 1  (mínimo)
print(max(numeros))         # 9  (máximo)
print(sum(numeros))         # 25 (suma total)

# Crear lista vacía y llenarla
lista_vacia = []
lista_vacia.append("primer elemento")


# ============================================================
# 7. FUNCIONES
# ============================================================
# Una función es un bloque de código reutilizable.
# Se define con def y se llama por su nombre.

# Función sin parámetros
def saludar():
    print("¡Hola!")

saludar()                   # ¡Hola!

# Función con parámetros
def saludar_persona(nombre):
    print(f"¡Hola, {nombre}!")

saludar_persona("Luis")     # ¡Hola, Luis!

# Función con valor por defecto
def saludar_con_titulo(nombre, titulo="Sr."):
    print(f"¡Hola, {titulo} {nombre}!")

saludar_con_titulo("Pérez")          # ¡Hola, Sr. Pérez!
saludar_con_titulo("García", "Dr.")  # ¡Hola, Dr. García!

# Función que retorna un valor
def sumar(a, b):
    return a + b

resultado = sumar(3, 5)
print(resultado)            # 8

# Función que retorna múltiples valores
def calcular(a, b):
    suma  = a + b
    resta = a - b
    return suma, resta

s, r = calcular(10, 3)
print(s, r)                 # 13 7


# ============================================================
# 8. DICCIONARIOS
# ============================================================
# Un diccionario guarda pares clave: valor.
# Se accede por clave, no por índice.

persona = {
    "nombre": "María",
    "edad": 30,
    "ciudad": "México"
}

# Acceder a valores
print(persona["nombre"])            # María
print(persona.get("edad"))          # 30
print(persona.get("email", "N/A"))  # N/A (valor por defecto si no existe)

# Agregar o modificar
persona["email"] = "maria@mail.com" # Agrega clave nueva
persona["edad"] = 31                # Modifica valor existente

# Eliminar
del persona["ciudad"]               # Elimina la clave "ciudad"

# Verificar si existe una clave
if "nombre" in persona:
    print("Tiene nombre")

# Recorrer un diccionario
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

# Obtener solo claves o solo valores
print(persona.keys())               # dict_keys(["nombre", "edad", ...])
print(persona.values())             # dict_values(["María", 31, ...])


# ============================================================
# 9. MANEJO DE ERRORES (try / except)
# ============================================================
# Evita que el programa se detenga ante un error.

try:
    numero = int(input("Escribe un número: "))
    resultado = 10 / numero
    print(f"Resultado: {resultado}")

except ValueError:
    print("Error: debes escribir un número válido.")

except ZeroDivisionError:
    print("Error: no se puede dividir entre cero.")

except Exception as e:
    print(f"Error inesperado: {e}")

finally:
    print("Esto siempre se ejecuta.")    # Opcional: se ejecuta siempre


# ============================================================
#  RESUMEN RÁPIDO DE MÉTODOS Y FUNCIONES MÁS USADAS
# ============================================================
#
#  STRINGS:         .upper() .lower() .strip() .replace()
#                   .split() .startswith() .endswith() len()
#
#  LISTAS:          .append() .insert() .remove() .pop()
#                   .sort() .reverse() len() in
#                   enumerate() min() max() sum()
#
#  DICCIONARIOS:    .get() .keys() .values() .items()
#                   del dict[key]  key in dict
#
#  CONVERSIÓN:      int() float() str() bool()
#
#  ENTRADA/SALIDA:  input()  print()  f"texto {variable}"
#
#  RANGOS:          range(fin)
#                   range(inicio, fin)
#                   range(inicio, fin, paso)
# ============================================================