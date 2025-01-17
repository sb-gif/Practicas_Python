"""
--------------------------- COLECCIONES ---------------------------
En este taller aprenderás a manipular coleccciones de datos: Listas, diccionarios, tuplas y sets.
"""
"""
 --- LISTAS ---
Las listas son ordenadas y mutables.
Pueden contener elementos duplicados.
Puedes modificar, añadir y eliminar elementos.
"""
"""
--- Ejercicio 1 Listas ---
Crea una variable "mascotas" que almacene una lista con los siguientes elementos: 'perro', 'gato', 'loro'
Imprime por consola el valor almacenado
Despues haz los pasos pedidos
"""
mascotas = ["perro", "gato", "loro"]
#print(mascotas)
    
# Escribe tu código aquí
# Escribe el código para saber la cantidad de elementos que tiene la lista, imprimir por consola
#print("Cantidad de elementos de la lista", len(mascotas))


# Escribe el código para acceder al valor de la posición 2, imprimir por consola
#print("posicion 2 de mi lista,", mascotas[1])

# Escribe el código para agregar una elemento a la lista, imprimir por consola la lista
#mascotas.append("pez")
#print("Añadir nuevo elemento a mi lista,", mascotas)


# Escribe el código para modificar un elemento de la lista, imprimir por consola la lista
#mascotas [0] = "caballo"
#print("Elemento modificado de mi lista,", mascotas)

# Escribe el código para eliminar un elemento de la lista, imprimir por consola la lista
#mascotas.remove("gato")
#print("Elemento de la lista eliminado,", mascotas)

#tambien podriamos eliminar un elemento de la lista con del
#del mascotasa([1])

"""
 --- TUPLAS ---
Las tuplas son ordenadas e inmutables.
Pueden contener elementos duplicados.
No puedes modificar, añadir o eliminar elementos después de la creación.
"""
"""
--- Ejercicio 2 Tuplas ---
Crea una variable "plantas" que almacene una tupla con los siguientes elementos: 'cactus', 'orquidea', 'rosas'
Imprime por consola el valor almacenado
Despues haz los pasos pedidos
"""
# Escribe tu código aquí
#plantas = ("cactus", "orquideas", "rosas")
#print(plantas)


# Escribe el código para saber la cantidad de elementos que tiene la tupla, imprimir por consola
#print("numero de elementos en nuestra tupla,",len(plantas))


# Escribe el código para acceder al valor de la posición 2, imprimir por consola
#print("valor de la posicion 2,", plantas[1])

# Intentar modificar una tupla
# plantas[1] = 'hoja rota'  # Descomenta esta línea para ver qué sucede

# Escribe tu análisís acá acerca de qué sucede
#da error de sintaxis porque las tuplas no se pueden modificar, son inmutables
"""
 --- SETS ---
Los sets son desordenados y mutables.
No pueden contener elementos duplicados.
Puedes añadir y eliminar elementos, pero no puedes modificar los elementos existentes.
"""
"""
--- Ejercicio 3 Sets ---
Crea una variable "nombres" que almacene un set con los siguientes elementos: 'María', 'Cris', 'Cris', 'Alex'
Imprime por la terminal dicha variable
Haz los pasos pedidos
"""
# Escribe el código aqui
#nombres = {"María", "Cris", "Cris", "Alex"}
#print(nombres)

# Explica qué sucede cuándo imprimes el valor que almacena "nombres"
#solo imprime una vez el nombre de Cris porque el conjunto no permite elementos duplicados

# Escribe el código para saber la cantidad de elementos que tiene el set, imprimir por consola
#print("numero de nombres en nuestro conjunto,",len(nombres))

# Escribe el código para acceder al valor de la posición 3, imprimir por consola
#print("valor de la posicion 3,", nombres[2])
#imprime en pantalla error porque los set no periten valores repetidos

# Escribe el código para agregar una elemento al set, imprimir por consola el set
#print("Añadir nuevo elemento a mi conjunto,", nombres)

# Escribe el código para eliminar un elemento del set, imprimir por consola el set
#nombres.remove("Cris")
#print("Elemento de la lista eliminado,", nombres)
#nombres.remove("Alex")
#print("Elemento de la lista eliminado,", nombres)

"""
 --- DICCIONARIOS ---
Los diccionarios son desordenados y mutables.
Contienen pares clave-valor.
Puedes añadir, modificar y eliminar pares clave-valor.
"""
"""
--- Ejercicio 4 Diccionarios ---
Crea un diccionario llamado "ciudad" con las claves 'nombre' y 'pais' y los valores 'Barcelona' y 'España' respectivamente.
Imprime el diccionario
"""
# Escribe el código aqui para acceder y ver por consola el valor de 'nombre'
Ciudad = {"Nombre": "Barcelona", "Pais": "España"}
print(Ciudad)
print(Ciudad["Nombre"])
# Escribe el código aqui para añadir un nuevo par clave-valor y ver por consola el valor de 'ciudad'
Ciudad["Código Postal"] = 8300
print(Ciudad)

# Escribe el código aqui para modificar el valor de un par clave-valor de 'ciudad' y verlo por consola
Ciudad["Nombre"] = "Madrid" 
print(Ciudad)

# Escribe el código aqui para eliminar un par clave-valor de 'ciudad' y verlo por consola
del Ciudad["Código Postal"] 
print(Ciudad)














