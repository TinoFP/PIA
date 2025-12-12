# Módulo PIA
# Tarea 1
# Ejercicio 2. Problema 1. Procesamiento de una lista de enteros. 
#
# Alumno: Angel Tinoco
#

def procesar_lista (lista):
    lista_procesada = []
    
    for num in lista:
        if num > 0:
             if num not in lista_procesada:
                lista_procesada.append(num)

    lista_procesada.sort()

    # Devuelve las 2 listas
    return lista_procesada


#########

# Ejemplo de uso
lista_numeros = [4, -1, 2, 4, 3, -5, 2]

solucion = procesar_lista(lista_numeros)

# Muestra las listas por pantalla
print ("La lista original es: ", lista_numeros)
print ("\nDespués de procesarla: ", solucion)

