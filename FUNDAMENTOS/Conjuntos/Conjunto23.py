'''
Comparar listas

Dadas dos listas, encuentra los elementos comunes.
'''
#creamos las listas
lista1 = [15, 20, 30, 25, 40, 23] 
lista2 = [15, 30, 40, 35, 55, 60]
#las convertimos a set
s1 = set(lista1)
s2 = set(lista2)

comunes = s1 & s2 #encontramos los comunes
#imprimimos las listas
print(f"La primera lista es: {lista1}")
print(F"La segunda lista es: {lista2}")
print(f"Los elementos comunes de la lista son: {list(comunes)}") #imprimimos los comunes de las listas
