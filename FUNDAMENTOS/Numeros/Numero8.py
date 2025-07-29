"""""
Raíz cuadrada y logaritmos:
Pide un número y calcula:
Su raíz cuadrada (math.sqrt(num)).
Su logaritmo natural (math.log(num)).
"""""""""
import math #Importamos la libreria math
numero = int(input("Digite un numero: ")) #Creamos la variable
#Creamos los calculos con la libreria
raiz_cuadrada = round(math.sqrt(numero), 2)
logaritmo_natural = round(math.log(numero), 2)
#Lo imprimimos
print(f"El numero es: {numero}")
print(f"La raiz cuadrada del numero es: {raiz_cuadrada}")
print(f"El logaritmo natural del numero es: {logaritmo_natural}")
