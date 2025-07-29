'''
Crear una tupla:

Define una tupla llamada colores con los valores ("rojo", "verde", "azul") e imprímela.

Intenta modificar el primer elemento a "amarillo" (debe generar un error por inmutabilidad).
'''
colores = ("rojo", "verde", "azul") #creamos la tupla

print(colores) #la imprimimos
colores[0] = ("amarillo") #intentamos modificar el primer elemento
