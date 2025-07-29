'''
Encontrar el máximo/mínimo:

Pide al usuario que ingrese 5 números, guárdalos en una lista y muestra el número mayor y menor (usa max() y min()).
'''
lista1 = [] #creamos la lista
for i in range(5): #Creamos un bucle de 0 a 5
    while True: #Creamos un while de que sea verdadero
        try: #creamos el try
             numeros = int(input(f"Ingrese 5 numeros enteros {i + 1}: ")) #le pedimos el numero al usuario
             lista1.append(numeros) #le añadimos los numeros a la lista
             break #lo rompemos
        except ValueError: #si no pone un numero entero
             print("Error! Debe ingresar un numero valido") #lo imprimimos

maximo = max(lista1) #vemos cual es el maximo de la lista
minimo = min(lista1) #vemos cual es el minimo de la lista  

print(f"La lista es: {lista1}") #imprimimos la lista
print(f"El maximo numero de la lista es: {maximo}") #imprimimos el maximo de la lista
print(f"El minimo de la lista es: {minimo}") #imprimimos el minimo de la lista
