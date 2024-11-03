# Módulo PIA
# Tarea 1
# Ejercicio 2. Problema 3: Conjuntos
#
# Alumno: Angel Tinoco
#


#########
# EJEMPLO DE USO

# Pide al usuario usuario valores para el primer conj

usuario = input ("Introduce varios números para el conjunto 1, separados por espacios.")
conjunto1 = set(map(int,usuario.split()))

usuario = input ("Introduce varios números para el conjunto 1, separados por espacios.")
conjunto2 = set(map(int,usuario.split()))

# Calcular la intersección
interseccion = conjunto1.intersection(conjunto2)
print("\nIntersección (están en ambos conjuntos):", interseccion)


# Calcular la unión
union = conjunto1.union(conjunto2)
print("\nUnión (se añaden los elementos de ambos conjuntos pero sin repetidos):", union)


# Calcular la diferencia simétrica
diferencia_simetrica = conjunto1.symmetric_difference(conjunto2)
print("\nDiferencia Simétrica (elementos en uno u otro, pero no en ambos):", diferencia_simetrica)


