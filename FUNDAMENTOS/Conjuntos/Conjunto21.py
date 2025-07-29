'''
Contar elementos únicos

Pide al usuario que introduzca números separados por espacios.

Calcula cuántos números únicos ingresó.
'''
n = int(input("Cuantos numeros quiere agregar: ")) #pedimos que diga cuantos numeros quiere introducir
numeros = [] #creamos la lista de numeros
for i in range(n): #creamos el bucle
    num = int(input(f"Introduzca el numero {i + 1}: ")) #decimos que introduzca el numero
    numeros.append(num) #añadimos el numero a la lista

unicos = set(numeros) #buscamos los numeros unicos

print(f"Los numeros son: {numeros}") #imprimimos la lista
print(f"Los numeros unicos son: {unicos}") #imprimimos los numeros unicos
print(f"La cantidad de numeros unicos es: {len(unicos)}") #imprimimos la cantidad de numeros unicos
