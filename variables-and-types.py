# VARIABLES / TIPOS DE DATOS ---------------------------
#En este taller aprenderás cómo crear variables, trabajar con diferentes tipos de datos.

#Ejercicio 1 Variables---
#Crea una variable llamada "mensaje". 
#Asígnale el valor "¡Hola, Mundo!". 
#Imprime el valor de la variable en la consola.

# Escribe tu código aquí

#mensaje = "¡Hola, Mundo!"
#print(mensaje)

"""
--- Ejercicio 2 Variables---
Invoca la variable anterior llamada "mensaje". 
Reasígnale el valor "Hello world!". 
Imprime el valor de la variable en la consola.
Escribe en un comentario de línea lo que sucede.
"""
# Escribe tu código aquí
#mensaje ="¡Hola Mundo!"
#mensaje ="¡hello word!"
#print(mensaje)

#imprime ambas variables, si queremos que solo salga hello word tenemos que borrar el mensaje del ejercicio 1
#hemos reasignado un nuevo valor a la variable mensaje , si queremso que solo salga hello word ponemos # en el ejercecio 1 para que no lo entienda
"""
--- Ejercicio 3 Tipos de datos---
Crea variables para cada uno de los siguientes tipos de datos y colecciones: string, int, float, 
bool, list, tuple, dicctionary and set. 
Imprime cada variable y el tipo de dato o colección que almacena en la consola.
"""
# Escribe tu código aquí
#string
var_string ="Hola"
print(var_string, type(var_string))

#entero (int)
var_entero =2025
print(var_entero, type(var_entero))

#decimal (float)
var_float =20.25
print(var_float, type(var_float))

#booleano
var_booleano =True
print(var_booleano, type(var_booleano))

#lista
var_lista =[3, 4, 4, "hola", 4.0, True]
print(var_lista, type(var_lista))
#print(f""Valor: {var_list})
print(var_lista [0], type(var_lista [0]))

#tupla
var_tupla =(10, 4, 5, "adios")
print(var_tupla, type(var_tupla))

#Diccionario
var_diccionario ={"clave1": "valor1", "clave2": 2}
print(var_diccionario,type(var_diccionario))

#conjunto set
var_set ={1, 2, 3, 4, 4}
print(var_set, type(var_set))

