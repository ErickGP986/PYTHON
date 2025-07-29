"""""
Área de un círculo:
Pide el radio y calcula el área con la fórmula:
area = math.pi * radio ** 2
(Usa import math).
"""""""""
import math #Importamos la libreria math
radio = float(input("cuanto es el radio del circulo: ")) #Creamos la variable radio y se la pedimos al usuario

area = round(math.pi * radio ** 2, 2) #Hacemos el calculo
#Lo imprimimos
print(f"El radio del circulo es: {radio} \ny su area es: {area}")
