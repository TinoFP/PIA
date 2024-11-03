# Módulo PIA
# Tarea 1
# Ejercicio 2. Problema 2: Frecuencia de las palabtas
#
# Alumno: Angel Tinoco
#


def contar_frecuencia_palabras(texto):
    # Convertir el texto a minúsculas
    texto = texto.lower()

    # Separar el texto completo en palabras, usando split con " " lo hace rápidamente
    lista_palabras = texto.split()

    # Usando una lista tipo diccionario para almacenar cada palabra y su frecuencia
    dic_frecuencia = {}
    for palabra in lista_palabras:
        if palabra in dic_frecuencia:
            dic_frecuencia[palabra] += 1
        else:
            dic_frecuencia[palabra] = 1

    # Ordenar el diccionario
    dic_frecuencia_ordenado = dict(sorted(dic_frecuencia.items()))

    # Mostrar las palabras y sus frecuencias ordenadas por "palabra"
    for palabra, frecuencia in dic_frecuencia_ordenado.items():
        print("Palabra: ",palabra,"(",frecuencia,")")

# fin DEF


#####################
# EJEMPLO DE USO
        
# Pide un texto al usuario
texto = input("Escribe texto para analizar: ")
contar_frecuencia_palabras(texto)
