'''
Contador de vocales:
Cuenta cuántas vocales (a, e, i, o, u) hay en una cadena ingresada por el usuario.

python
texto = input("Ingresa un texto: ").lower()
vocales = texto.count('a') + texto.count('e') + texto.count('i') + texto.count('o') + texto.count('u')
print("Total de vocales:", vocales)
'''
texto = input("Ingrese un texto: ").lower() #Le pedimos una cadena al usuario y lo pasamos a minusculas
vocales = texto.count('a') + texto.count('e') + texto.count('i') + texto.count('o') + texto.count('u') #Contamos las vocales de la cadena

print("La cadena es: ", texto) #Imprimimos la cadena de textp
print("Total de vocales: ", vocales) #Imprimimos cuantas vocales tiene
