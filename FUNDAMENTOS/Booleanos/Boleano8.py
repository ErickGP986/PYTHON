'''
Validación de contraseña segura:
Muestra True si una contraseña tiene:

Al menos 8 caracteres.

Al menos una mayúscula y una minúscula.
(Pista: Usa any(c.isupper() for c in contraseña) y len()).
'''
def es_contraseña_segura(contraseña): #Creamos una funcion que resguarde
    if len(contraseña) < 8: #Creamos una condicion de menos de 8 caracteres
        return False #regresa falso
    tiene_mayuscula = any(c.isupper() for c in contraseña) #revisa si algun caracter es mayuscula
    tiene_minusucula = any(c.islower() for c in contraseña) #revisa si algun caracter es minuscula
    return tiene_mayuscula and tiene_minusucula #Lo regresamos

contraseña = input("Ingrese su contraseña: ") #Le pedimos la contraseña al usuario
print(" ¿Es segura? ", es_contraseña_segura(contraseña)) #Lo imprimimos
