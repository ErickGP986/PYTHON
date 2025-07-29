'''
Suma de elementos:

Dada una lista de números [5, 10, 15, 20], calcula la suma de todos sus elementos (usa un bucle o la función sum()).
'''
numeros = [5, 10, 15, 20] #Creamos la lista
suma = 0 #creamos la variable y la igualamos a 0
for i in numeros: #creamos el bucle para sumar los numeros
    suma += i #sumamos los numeros de la lista

print(f"suma de la lista en bucle: {suma}") #imprimimos el resultado

suma_lista = sum(numeros) #creamos una variable que almacene la suma de la lista numeros

print(f"lista con funcion sum: {suma_lista}") #Imprimimo la suma de la lista
