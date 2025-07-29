"""""
Binario, hexadecimal y octal:
Pide un número entero y conviértelo a:
Binario (bin(numero)).
Hexadecimal (hex(numero)).
Octal (oct(numero)).
"""""""""
numero = int(input("Ingrese un numero: ")) #creamos una variable y la pedimos al usuario
#creamos las variables que almacenen los nuemros binarios, hexadecimales y octal
numero_binario = bin(numero)
numero_hexadecimal = hex(numero)
numero_octal = oct(numero)
#lo imprimmos 
print(f"El numeroo es: {numero}")
print(f"El numero en binario es: {numero_binario}")
print(f"El numero en hexadecimal es: {numero_hexadecimal}")
print(f"El numero en octal es: {numero_octal}")
