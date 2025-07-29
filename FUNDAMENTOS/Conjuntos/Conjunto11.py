'''
Eliminar duplicados

Dada una lista con elementos duplicados:

lista = [1, 2, 2, 3, 4, 4, 4, 5]
Convierte la lista en un set para eliminar duplicados.

Vuelve a convertirlo en lista.
'''
lista = [1, 2, 2, 3, 4, 4, 4, 5] #creamos la lista

convertida = list(set(lista)) #convertimos la lista a set y lista a la vez

print(f"La lista es: {lista}") #imrimmimos la lista
print(f"Eliminar duplicados: {convertida}") #imprimimos la lista sin duplicados
