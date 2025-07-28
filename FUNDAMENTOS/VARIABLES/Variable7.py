"""""
Manipulación de Strings
Dada una variable texto = "Python es genial":
Imprime la longitud del string.
Convierte el texto a mayúsculas.
Reemplaza "genial" por "poderoso".
"""""""""
#Creamos las variables
texto = "Python es genial"
frase_corregida = texto.replace("genial", "poderoso") #corregimos el texto

#imprimimos el resultado
print("La longitud de la cadena es: ", len(texto))
print("La cadena en Mayusculas: ", texto.upper())
print("La cadena corregida: ", frase_corregida)
