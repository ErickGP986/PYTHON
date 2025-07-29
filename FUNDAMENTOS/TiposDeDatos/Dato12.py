"""""
Desempaquetado:
Dada la tupla coordenadas = (4, 5), 
desempaquétala en variables x e y y calcula la distancia al origen (fórmula: √(x² + y²)).
"""""""""
import math #Importar la libreria math 
coordenadas = (4, 5) #Creamos la tupla 

(x, y) = coordenadas #La desempaquetamos 

distancia_origen = round(math.sqrt(x**2 + y**2), 2) #Hacemos el calculo y lo redondeamos a 2

print(f"las coordenadas son: {coordenadas} y el calculo de la distancia al origen es: {distancia_origen}") #Lo imprimimos
