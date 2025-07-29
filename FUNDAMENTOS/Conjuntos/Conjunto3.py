'''
Verificar pertenencia:

Pide al usuario una letra y verifica si está en el set vocales (usa in).
'''
vocales = {"a", "e", "i", "o", "u"} #creams el conjunto

letra = input("Ingrese una letra: ") #pedimos al usuario la letra
#creamos la condicional para ver si la letra esta en el conjunto
if letra in vocales:
    print(f"la letra: {letra} si esta en: {vocales}")#imprimimos si es verdad
else:
    print(f"La letra no esta en vocales....") #imprimimos si no es verdad
