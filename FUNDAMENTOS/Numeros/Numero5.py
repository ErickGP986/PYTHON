"""""
Conversión de unidades:
Convierte:
Kilómetros a millas (1 km = 0.621371 millas).
Celsius a Fahrenheit (F = (C × 9/5) + 32).
"""""""""
Kilometros = float(input("Cuantos kilometros son: ")) #Creamos la variable de kilometros
celcius = float(input("Cuanto es la temperatura en celcius: ")) #Creamos la variable de celcius
#Hacemos los calculos
millas = round(Kilometros * 0.621371, 2)
F = round((celcius * 9/5) + 32, 2)
#Lo imprimimos
print(f"Los kilometros son: {Kilometros} y a millas son: {millas}")
print(f"La temperatura celcius: {celcius} convertido a farenheit es: {F}")
