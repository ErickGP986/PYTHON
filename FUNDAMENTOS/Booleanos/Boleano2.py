'''
Igualdad de strings:
Pide dos palabras y muestra True si son iguales (ignorando mayúsculas/minúsculas).

python
palabra1 = input("Palabra 1: ").lower()
palabra2 = input("Palabra 2: ").lower()
print(palabra1 == palabra2)
'''
palabra1 = input("Ingrese la primera palabra: ").lower() #Le pedimos la primera palabra al usuario
palabra2 = input("Ingrese la segunda palabra: ").lower() #Le pedimos la segunda palabra al usuario

print(palabra1 == palabra2) #Hacemos la comparacion entre las dos palabras y vemos si son iguales
