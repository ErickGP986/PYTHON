'''
Eliminar duplicados:

Dada la lista [1, 2, 2, 3, 4, 4, 5], crea una nueva lista sin elementos repetidos (usa set() o un bucle).
'''
lista = [1, 2, 2, 3, 4, 4, 5] #creamos la lista

lista_sin_repeticiones = list(set(lista)) #usamos la funcion set 
nueva_lista = [] #creamos una nueva lista

for elemento in lista: #creamos un for que pase por la lista
    if elemento not in nueva_lista: #si los elementos de la nueva lista no existe
        nueva_lista.append(elemento) #los añade

print(f"La lista original es: {lista}") #imprimimos la lista
print(f"La lista con set: {lista_sin_repeticiones}") #imprimimos la lista con set
print(f"la lista con el bucle: {nueva_lista}") #imprimimios la lista con bucle
