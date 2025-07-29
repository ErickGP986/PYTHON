'''
Año bisiesto:
Un año es bisiesto si:

Es divisible entre 4 pero no entre 100.

O es divisible entre 400.
Pide un año y muestra True si es bisiesto.

python
año = int(input("Año: "))
print((año % 4 == 0 and año % 100 != 0) or (año % 400 == 0))
'''
año = int(input("Ingrese el año: ")) #Le pedimos el año al usuario

if(año % 4 == 0 and año % 100 != 0 or año % 400 == 0): #Creamos la condicion
    print(f"El año {año} es bisiesto.") #Lo imprimimos
else:
    print(f"el año: {año} no es bisiesto.") #Si no decimos que no es bisiesto
