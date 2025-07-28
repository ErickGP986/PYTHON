"""""
Área y Perímetro
Pide al usuario el radio de un círculo y calcula:
El área (A = π * r²).
El perímetro (P = 2 * π * r).
Usa math.pi para el valor de π.
"""""""""
import math #Importamos el modulo math

radio = float(input("Digite el radio del circulo: ")) #creamos la variable y se la pedimos al Usuario

Area = math.pi * radio * radio #Calculamos el Area

perimetro = 2 * math.pi * radio #Calculamos el perimetro
#Imprimimos el resultado
print(f"El radio es: {radio}")
print(f"El Area es: {Area:.2f}")
print(f"El perimetro del circulo es: {perimetro:.2f}")
