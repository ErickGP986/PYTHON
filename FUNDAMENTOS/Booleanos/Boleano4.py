'''
Rango de números:
Pide un número y verifica si está entre 10 y 20 (incluyendo ambos).

python
numero = int(input("Número: "))
print(10 <= numero <= 20)  # Alternativa: (numero >= 10) and (numero <= 20)
'''
numero = int(input("Ingrese un numero: ")) #le pedimos el numero al usuario

if(numero >= 10 and numero <= 20): #Creamos la condicion
    print(f"El numero: {numero} esta en el rango.") #decimos si el numero esta en el rango
else:
    print(f"El numero: {numero} no esta en el rango.") #decimos si el numero no esta en el rango
