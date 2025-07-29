'''
Número par y positivo:
Pide un número y muestra True si es par y positivo.

python
numero = int(input("Número: "))
print(numero % 2 == 0 and numero > 0)
'''
numero = int(input("Ingrese un numero: ")) #Le pedimo el numero al usuario

if(numero % 2 == 0 and numero > 0): #Creamos la condicion de si es par y positivo
    print(f"El numero: {numero} es par y positivo.") #Lo imprimimos
elif(numero % 2 == 1 and numero > 0): #creamos la condicion de no es par pero si positivo
    print(f"El numero: {numero} no es par, pero si positivo.") #lo imprimimos
elif(numero % 2 == 0 and numero < 0): #creamos la condicion de que es par pero no positivo
    print(f"El numero: {numero} si es par, pero no positivo") #lo imprimimos
elif(numero % 2 == 1 and numero < 0): #creamos la condicion de que no es par pero tampoco positivo
    print(f"El numero: {numero} no es par, ni positivo") #lo imprimimos
