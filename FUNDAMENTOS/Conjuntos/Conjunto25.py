'''
Eliminar elementos duplicados de una lista de listas

Tip: Convierte cada sublista en tuple y luego usa un set de tuplas.
'''
lista = [[1, 2, 2, 4], [1, 3, 3, 4,], [5, 10, 10, 12]] #creamos la lista con sublista

lista_de_tuplas = [tuple(sublista) for sublista in lista] #volvemos la lista en tuplas

tuplas_unicas = set(lista_de_tuplas) #buscamos los elementos unicos

lista_unica = [list(tupla) for tupla in tuplas_unicas] #volvemos la tupla a listas

print(lista_unica) #lo imprimimos
