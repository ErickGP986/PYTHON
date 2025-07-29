"""""
Conversión de temperatura:
Pide al usuario una temperatura en Celsius y conviértela a Fahrenheit usando la fórmula:
fahrenheit = (celsius * 9/5) + 32  
"""""""""
celcius = float(input("Digite la temperatura en celcius: ")) #Creamos la variable y le pedimos la temperatura en celcius al usuario

fahrenheit = round((celcius * 9/5) + 32, 2) #Lo calculamos a fahrenheit redondeado a 2

print(f"La temperatura Celcius es: {celcius} convertida a fahrenheit es: {fahrenheit}") #Imprimimos el rsultado
