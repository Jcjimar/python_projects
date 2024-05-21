""" 
- Vamos a crear un programa que gestione listas de reproducción de música utilizando conjuntos y las funciones/métodos que hemos aprendido.
    1. Define dos listas de reproducción iniciales, **`playlist_a`** y **`playlist_b`**, cada una con al menos cinco canciones representadas por nombres de canciones (strings).
    2. Crea conjuntos a partir de estas listas de reproducción.
    3. Implementa la funcionalidad para agregar una nueva canción a una lista de reproducción.
    4. Implementa la funcionalidad para eliminar una canción de una lista de reproducción.
    5. Utiliza el método de conjunto **`union`** para crear una nueva lista de reproducción que contenga todas las canciones de **`playlist_a`** y **`playlist_b`**.
    6. Utiliza el método de conjunto **`intersection`** para crear una nueva lista de reproducción que contenga solo las canciones que están en ambas **`playlist_a`** y **`playlist_b`**.
    7. Utiliza el método de conjunto **`difference`** para crear una nueva lista de reproducción que contenga las canciones que están en **`playlist_a`** pero no en **`playlist_b`**.
    8. Imprime las listas de reproducción resultantes y verifica que las funcionalidades y métodos están trabajando correctamente.
"""
# 1. Defino las listas de reproducción iniciales con canciones de los 80's
playlist_a = ["Mar antiguo","Billie Jean","El ataque de los chicos cococdrilos","Ni tu ni nadie", "Take On Me","Sueltate el pelo", "Sweet Child O' Mine", "Como un burro amarrado en la puerta del baile " ,"Every Breath You Take", "La flaca", "Livin' On A Prayer", "Carolina", "Girls Just Want to Have Fun", "Corazón partío"]
playlist_b = ["Voy a pasármelo bien", "Se acabó","Like A Virgin", "20 de abril",  "Another One Bites The Dust", "A quien le importa", "La chica de ayer" "Eye Of The Tiger", "Amiga mía", "Every Little Thing She Does Is Magic", "Laura no está", "Hungry Like The Wolf", "Y, ¿si fuera ella?", "Every Rose Has Its Thorn", "Depende", "Cuentame un cuento"]

# 2. Creo conjuntos a partir de las listas de reproducción
conjunto_a = set(playlist_a)
conjunto_b = set(playlist_b)

# 3. Agrego una nueva canción a una lista de reproducción
nueva_cancion_a = str(input("\nIngrese el nombre de una nueva canción para Playlist A de los 80's:\n\n")).title()
conjunto_a.add(nueva_cancion_a)

nueva_cancion_b = input("\nIngrese el nombre de una nueva canción para Playlist B de los 80's:\n\n").title()
conjunto_b.add(nueva_cancion_b)

# 4. Elimino una canción de una lista de reproducción utilizando discard()
eliminar_cancion_a = str(input("\nIngrese el nombre de una canción para eliminar de Playlist A de los 80's:\n\n")).title()
conjunto_a.discard(eliminar_cancion_a)

eliminar_cancion_b = str(input("\nIngrese el nombre de una canción para eliminar de Playlist B de los 80's:\n\n")).title()
conjunto_b.discard(eliminar_cancion_b)

# 5. Creo una nueva lista de reproducción con todas las canciones
nueva_playlist_todas = conjunto_a.union(conjunto_b)

# 6. Creo una nueva lista de reproducción con canciones en común
nueva_playlist_comunes = conjunto_a.intersection(conjunto_b)

# 7. Creo una nueva lista de reproducción con canciones en playlist_a pero no en playlist_b
nueva_playlist_diferencia = conjunto_a.difference(conjunto_b)

# 8. Imprimo las listas de reproducción resultantes
print("Lista de Reproducción A:", conjunto_a)
print("Lista de Reproducción B:", conjunto_b)
print("Lista de Reproducción Todas:", nueva_playlist_todas)
print("Lista de Reproducción Comunes:", nueva_playlist_comunes)
print("Lista de Reproducción Diferencia:", nueva_playlist_diferencia)