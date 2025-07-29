"""""
Manipulación de texto:
Dado el string s = "Aprendiendo Python":
Imprime su longitud.
Extrae la palabra "Python" (usando slicing).
Reemplaza "Python" por "programación".
Convierte todo a mayúsculas.
"""""""""
s = "Aprendiendo Python" #Creamos la cadena
longitud_texto = len(s) #digitamos la longitud de la variable
remplazo_texto = s.replace("Python", "programacion") #Replazamos python por programacion
texto_mayusculas = s.upper() #Lo pasamos a mayusculas
#Lo imprimmimos
print("El texto original es: ", s)
print("La longitud de la cadena es: " ,longitud_texto)
print("Extracion de la palabra: " , s[0:11])
print("El texto remplazado es: ", remplazo_texto)
print("El texto en mayusculas: ", texto_mayusculas)
