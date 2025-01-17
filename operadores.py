"""
--------------------------- OPERADORES ---------------------------
En este taller aprenderás usar los diferentes tipos de operadores
"""
"""
--- Ejercicio 1 operadores aritméticos  ---
Reemplaza el ? con el operador según sea el caso
"""
num1 = 10
num2 = 5
# print(f"Suma: {num1 ? num2}")
#print(f"Suma: {num1 + num2}")

# print(f"Resta: {num1 ? num2}")
#print(f"Resta: {num1 - num2}")

# print(f"Multiplicación: {num1 ? num2}")
#print(f"Multiplicación: {num1 * num2}")

# print(f"División: {num1 ? num2}")
# print(f"División: {num1 / num2}")

"""
--- Ejercicio 2 operadores lógicos  ---
Reemplaza el ? con el operador según sea el caso
Puedes investigar sobre las tablas de la verdad, recuerda "las amigas de mis amigas, son mis amigas"
"""
michi_4_patas = True
michi_3_ojos = False
michi_vuela = False
michi_interesado = True
michi_juega = True
michi_pone_huevos = False

# print(f"AND: {michi_4_patas ? michi_3_ojos}")
#print(f"AND: {michi_4_patas and michi_3_ojos}")
#en terminal nos dice falso porque si tiene 4 patas pero no tiene 3 ojos

# print(f"OR: {michi_interesado ? michi_vuela}")
#print(f"OR: {michi_interesado or michi_vuela}")
#nos sale en pantalla falso porque aunque es interesado no vuela

# print(f"NOT bool1: {? michi_juega}")
#print(f"NOT bool1: {not michi_juega}")
#imprime el valor invertido de michi juega, como es verdadero sale falso

# print(f"NOT bool2: {? michi_pone_huevos}")
#print(f"NOT bool2: {not michi_pone_huevos}")
#imprime en pantalla el valor invertido de michi pone huevos, por tanto como no es verdad el valor invertido es verdadero

"""
--- Ejercicio 3 Comparadores  ---
Reemplaza el ? con el comparador según sea el caso
"""
a = 7
b = 3
# print(f"¿a es igual a b?: {a ? b}")
print(f"a es igual a b: ", (a == b))
#imprime en pantalla false porque a y b son diferentes

# print(f"¿a es diferente de b?: {a ? b}")
#print(f"a es diferente de b:", (a != b))
#en pantalla sale true pq a y b son diferentes

# print(f"¿a es mayor que b?: {a ? b}")
#print(f"a es mayor que b:", (a > b))
#imprime en pantalla true pq es verdad

# print(f"¿a es menor que b?: {a ? b}")
print(f"a es menor que b:", (a < b))
#imprime en pantalla falso pq no es verdad

# print(f"¿a es mayor o igual que b?: {a ? b}")
#print(f"a es mayor o igual que b:", (a >= b))
#imprime en pantalla true pq es verdad

# print(f"¿a es menor o igual que b?: {a ? b}")
#print(f"a es menor o igual que b:", (a <= b))
#imprime en pantalla falso pq no es verdad