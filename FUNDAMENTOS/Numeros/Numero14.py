"""""
String a número:
Pide al usuario un número como string (ej: "123") y conviértelo a int y float.
"""""""""
numero = input("Ingrese un numero: ") #Creamos la variable y se la pedimos al usuario
#los convertimos a int y float, las almacenamos en otras variables
conversion_int = int(numero)
conversion_float = float(numero)
#Lo imrpimimos
print(f"El numero en string es: {numero}")
print(f"El numero convertido a int es: {conversion_int}")
print(f"El numero convertido a float es: {conversion_float}")
