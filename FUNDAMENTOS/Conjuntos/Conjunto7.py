'''
Eliminar duplicados de una lista:

Convierte la lista [1, 2, 2, 3, 4, 4, 5] en un set para eliminar duplicados y luego vuélvela a lista.
'''
lista = [1, 2, 2, 3, 4, 4, 5] #creamos la lista

lista_conjunto = set(lista) #pasamos la lista a conjunto con set
conjunto_lista = list(lista_conjunto) #pasamos el conjunto a lista con list

print(f"La lista original es: {lista}") #imprimimos la lista original
print(f"La lista convertida a conjunto es: {lista_conjunto}") #imprimimos la lista convertida a conjunto
print(f"El conjunto convertido a lista es: {conjunto_lista}") #imprimimos el conjunto convertido a lista
