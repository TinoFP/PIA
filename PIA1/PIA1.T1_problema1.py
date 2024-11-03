# Módulo PIA
# Tarea 1
# Ejercicio 2. Problema 1: Dividir una lista en 2 listas sepadas de números negativos y positivos
#
# Alumno: Angel Tinoco
#

def separar_listas (lista):
    num_positivos = []
    num_negativos = []
    for num in lista:
        if num < 0:
            num_negativos.append(num)
        else:
            num_positivos.append(num)

    num_positivos.sort()
    num_negativos.sort()

    # Devuelve las 2 listas
    return num_negativos, num_positivos


#########

# Ejemplo de uso
lista_numeros = [-10,-2,7,5,-8,10]

lista_negativos, lista_positivos = separar_listas(lista_numeros)

# Muestra las listas por pantalla
print ("La lista original es: ", lista_numeros)
print ("\nDespués de procesarla:\n")
print ("Lista de números negativos: \n", lista_negativos)
print ("Lista de números positivos: \n", lista_positivos)

