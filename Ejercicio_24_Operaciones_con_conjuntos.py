""" 
Escribe un programa en Python que realice las siguientes operaciones con conjuntos:

1. **Creación de conjuntos:**
    - Crea dos conjuntos llamados **`set1`** y **`set2`** con al menos tres elementos cada uno.
2. **Unión de conjuntos:**
    - Realiza la unión de los conjuntos **`set1`** y **`set2`** y almacena el resultado en un nuevo conjunto llamado **`union`**.
3. **Intersección de conjuntos:**
    - Encuentra la intersección entre los conjuntos **`set1`** y **`set2`** y almacena el resultado en un nuevo conjunto llamado **`interseccion`**.
4. **Diferencia de conjuntos:**
    - Encuentra la diferencia entre los conjuntos **`set1`** y **`set2`** (elementos en **`set1`** pero no en **`set2`**) y almacena el resultado en un nuevo conjunto llamado **`diferencia`**.
5. **Diferencia simétrica de conjuntos:**
    - Encuentra la diferencia simétrica entre los conjuntos **`set1`** y **`set2`** (elementos que están en uno de los conjuntos pero no en ambos) y almacena el resultado en un nuevo conjunto llamado **`diferencia_simetrica`**.
6. **Subconjunto:**
    - Verifica si el conjunto **`set1`** es un subconjunto del conjunto **`set2`** y muestra el resultado.
7. **Superconjunto:**
    - Verifica si el conjunto **`set1`** es un superconjunto del conjunto **`set2`** y muestra el resultado.
8. **Mostrar resultados:**
    - Muestra los conjuntos resultantes **`union`**, **`interseccion`**, **`diferencia`** y **`diferencia_simetrica`**, así como los resultados de las verificaciones de subconjunto y superconjunto.
"""
# Creación de conjuntos
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Unión de conjuntos
union = set1.union(set2)

# Intersección de conjuntos
interseccion = set1.intersection(set2)

# Diferencia de conjuntos (set1 - set2)
diferencia = set1.difference(set2)

# Diferencia simétrica de conjuntos
diferencia_simetrica = set1.symmetric_difference(set2)

# Verificar si set1 es un subconjunto de set2
es_subconjunto = set1.issubset(set2)

# Verificar si set1 es un superconjunto de set2
es_superconjunto = set1.issuperset(set2)

# Mostrar resultados
print("Unión de conjuntos:", union)
print("Intersección de conjuntos:", interseccion)
print("Diferencia de conjuntos (set1 - set2):", diferencia)
print("Diferencia simétrica de conjuntos:", diferencia_simetrica)
print("¿set1 es un subconjunto de set2?", es_subconjunto)
print("¿set1 es un superconjunto de set2?", es_superconjunto)
