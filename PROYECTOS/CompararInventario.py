'''
Comparador de inventarios

Dos tiendas tienen listas de productos.

Crea un script que:

Muestra los productos comunes.

Muestra los productos exclusivos de cada tienda.

Muestra todos los productos sin duplicados.
'''
#creamos las listas de los productos
productos1 = [] 
productos2 = []

print("===INGRESO DE PRODUCTOS - TIENDA 1 ===") #le decimos que ingrese los productos de la primera tienda
while True: #creamos una lista dinamica
    entrada_1 = input("Que productos desea poner de la primera tienda (escriba fin para terminar.): ").strip() #le decimos que introduzca los productos
    if entrada_1.lower() == 'fin': #si dice fin
       break #termina
    productos1.append(entrada_1.lower()) #se le añaden los productos a la lista

print("===INGRESO DE PRODUCTOS - TIENDA 2 ===") #ahora le pedimos los productos de la segunda tienda
while True: #creamos la lista dinamica
    entrada_2 = input("Que productos quieres poner de la segunda tienda (escriba fin para terminar): ").strip() #le pedimos al usuario qu eintroduzca los productos
    if entrada_2.lower() == 'fin': #si escibe fin
        break #termina
    productos2.append(entrada_2.lower()) #le añadimos los productos a la lista
#creamos los conjuntos
tienda1 = set(productos1) 
tienda2 = set(productos2) 
comunes = tienda1.intersection(tienda2) #vemos cuales son los comunes en las tiendas
exclusivo1 = tienda1.difference(tienda2) #vemos cuales son los exclusivos de la tienda 1
exclusivo2 = tienda2.difference(tienda1) #vemos cuales son los exclusivos de la tienda 2
todos = tienda1 | tienda2 #unimos los productos de las 2 tiendas

print("\n===RESULTADOS===") #le decimos cuales son sus resultados
print("\nProductos comunes en ambas tiendas:") #le decimos cuales son los productos comunes
print(sorted(comunes) if comunes else "No hay productos comunes") #le decimos si no hay productos comunes

print("\nExculsivos de la tienda 1:") #le decimos cuales son los productos exclusivos de la primera tienda
print(sorted(exclusivo1) if exclusivo1 else "No hay productos exclusivos") #le decimos si no hay exclusivos

print("\nExculsivos de la tienda 2:") #le decimos cuales son los productos exclusivos de la segunda tienda
print(sorted(exclusivo2) if exclusivo2 else "No hay productos exclusivos") #le decimos si no hay exclusivos

print("\nTodos los productos unicos:") #le enseñamos todos los productos
print(sorted(todos)) #los imprimimmos
