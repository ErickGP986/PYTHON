'''
Congelación (frozenset)

Crea un frozenset a partir de una lista.

Intenta agregar un elemento y observa qué pasa.
'''
lista = [2, 3, 4, 6, 8, 10] #creamos la lista
congelado = frozenset(lista) #congelamos la lista

lista.add(11) #vemos que al añadirle una lista aparece error
