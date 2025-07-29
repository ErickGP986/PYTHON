'''
Convertir entre lista y tupla:

Convierte la lista [1, 2, 3] a tupla y viceversa (usa tuple() y list()).
'''
numeros = [1, 2, 3] #creamos la lista

nueva_tupla = tuple(numeros) #pasamos la lista a tupla
nueva_lista = list(numeros) #pasamos la tupla a lista nuevamente

print(f"la lista original es: {numeros}") #imprimimos la lista
print(f"la lista convertida a tupla es: {nueva_tupla}") #imprimimos la tupla
print(f"la tupla convertida a lista es: {nueva_lista}") #imprimimos la tupla ocnvertida a lista
