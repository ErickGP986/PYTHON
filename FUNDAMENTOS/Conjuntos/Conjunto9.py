'''
Filtrar elementos comunes:

Pide al usuario dos listas de números, conviértelas a sets y muestra los números que aparecen en ambas.
'''
#creamos las listas
lista1 = []
lista2 = []
#pedimos cuantos numeros quiere para la primera lista
n = int(input("cuantos numeros desea agregar a la primera lista: "))
for i in range(n): #creamos el bucle para que recorra deacuerdo a los numereos que quiera agregar
    numero1 = int(input(f"que numero quiere agregar {i + 1}: ")) #le pedimos al usuario que agregue el numero
    lista1.append(numero1) #se lo añadimos a la lista
#repetimos el mismo proceso
x = int(input("cuantos numeros desea agregar a la segunda lista: "))
for i in range(x):
    numero2 = int(input(f"Que numero quiere agregar {i + 1}: "))
    lista2.append(numero2)
#convertimos las listas a conjuntos
conjunto1 = set(lista1) 
conjunto2 = set(lista2)
#las imprimimos
print(f"El primer conjunto es: {conjunto1}")
print(f"El segundo conjunto es: {conjunto2}")
