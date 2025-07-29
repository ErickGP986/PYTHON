'''
Generador de Contraseñas (Avanzado)
Descripción: Crea contraseñas aleatorias con letras, números y símbolos.
Habilidades usadas:

Módulo random (choice o shuffle).
'''
import random #Importamos random
import string as s #Importamos string para el codigo ascii

def generar_contraseña(longitud): #Definimos la funcion
    caracteres = s.ascii_letters + s.digits + s.punctuation #creamos una variable que guarde todo los que nos pide 
    psw = ''.join(random.choice(caracteres) for i in range(longitud)) #Creamos la contraseña
    return psw #Regresamos la contraseña

longitud = int(input("Longitud de contraseña: ")) #Le pedimos de que longituda al usuario
contraseña = generar_contraseña(longitud) #Llamamos a la funcion 
print("Contraseña: ", contraseña) #La imprimimos
