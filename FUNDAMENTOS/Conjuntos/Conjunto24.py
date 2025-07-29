'''
Encontrar diferencias entre listas

Dadas dos listas, muestra qué elementos de la primera no están en la segunda.
'''
#creamos las listas
lista1 = [15, 20, 30, 25, 40, 23]
lista2 = [15, 30, 40, 35, 55, 60]
#los convertimos a set
s1 = set(lista1)
s2 = set(lista2)

comunes = s1 - s2 #buscamos la difernecia entre listas
#imprimimos las listas
print(f"La primera lista es: {lista1}")
print(F"La segunda lista es: {lista2}")
print(f"Los elementos diferetes de la lista son: {list(comunes)}") #imprimimos los diferentes elementos
