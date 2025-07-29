'''
Eliminar duplicados de una cadena

Pide al usuario una frase.

Extrae los caracteres únicos.
'''
texto = input("Ingrese una cadena de texto: ") #le pedimos al usuario que ingrese la cadena

caracteres_unicos = set(texto) #buscamos los caracteres unicos

print(f"El texto es: {texto}") #imprimimos el texto
print(f"Los caracteres unicos son: {caracteres_unicos}") #imprimimos los caracteres unicos
