"""""
Conversión de Tipos
Pide al usuario que ingrese un número como string (ej: "15"), conviértelo a entero y súmale 5.
Luego, pide un float (ej: "3.14"), conviértelo y multiplícalo por 2.
"""""""""
#Creamos las variables
Numero = input("Digite un numero entero: ")
Numero2 = input("Digite un numero decimal: ")

Conversion1 = int(Numero) + 5 #La convertimos a int
Conversion2 = float(Numero2) * 2 #La convertimos a float
#Imprimimos los resultados
print(f"Los numeros son: {Numero} y {Numero2}")
print("La primera conversion es: ", Conversion1)
print("La segunda conversion es: ", Conversion2)
