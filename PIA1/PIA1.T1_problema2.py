# Módulo PIA
# Tarea 1
# Ejercicio 2. Problema 2. Frecuencia de palabras en un texto.
#
# Alumno: Angel Tinoco
#

# Librerias
import os
import string


def frecuencia_palabras(iPalabras, iFichero):
    # CHEQUEOS PREVIOS ---------------------------
    if iPalabras == "":
        print("ERROR: No has indicado ninguna palabra para analizar su frecuencia.")
        exit (1)
    


    # Analiza si existe el fichero
    if os.path.exists(iFichero):

        # COMIENZA EL PROCESAMIENTO -------------------
     
        # Usando una lista tipo diccionario para almacenar cada palabra y su frecuencia
        dic_frecuencia = {}

        # Lee el fichero y lo procesa
        try:
            with open(iFichero,"r") as f:
                
                # Convertir las palabras a analizar minúsculas
                iPalabras= iPalabras.lower()
                contenido_fich = f.read().lower()

                # quita signos de puntuacion
                iPalabras = iPalabras.translate(str.maketrans("","",string.punctuation))
                contenido_fich = contenido_fich.translate(str.maketrans("","",string.punctuation))

                # Separar el texto completo en palabras, usando split con " " lo hace rápidamente
                lista_palabras = iPalabras.split()
                contenido_fich = contenido_fich.split()

                # Inicializa el diccionario. Doy de alta todas las palabras buscadas, si no aparecen
                # en el texto, se pone un 0.
                for palabra in lista_palabras:
                    dic_frecuencia[palabra] = 0

               
                # Lee el contenido del texto.
                for palabra in contenido_fich:
                    # busca cada palabra
                    if palabra in lista_palabras:
                        # Si encuentra la palabra, aumenta la frecuencia
                        if palabra in dic_frecuencia:
                            dic_frecuencia[palabra] += 1


        except PermissionError:
            print(f"ERROR: No tienes permisos para abrir el fichero '{iFichero}'.")
        except IOError as e:
            print(f"Ocurrió un error de E/S inesperado: {e}")
    else:
        print ("ERROR: El fichero "+iFichero+" no existe.")
        exit(2)
    # Fin IF

    
    # Ordenar el diccionario
    dic_frecuencia_ordenado = dict(sorted(dic_frecuencia.items()))

    # Mostrar las palabras y sus frecuencias ordenadas por "palabra"
    for palabra, frecuencia in dic_frecuencia_ordenado.items():
        print("Palabra: ",palabra,"(",frecuencia,")")

# fin DEF


#####################
# EJEMPLO DE USO
        
# Pide una lista de palabras al usuario
palabras = input("Escribe las palabras que quieras contar: ")
fichero = input("Indica la ruta del fichero a procesar: ")
print ("\n\n")

# EJEMPLO PRUEBAS
# palabras = "prueba 2 fichero de texto"
# fichero = "/home/tino/Escritorio/GIT/PIA/PIA1/texto_problema2.txt"

# Ejecuta la función
frecuencia_palabras(palabras, fichero)

