"""
Validación de email (básico):
Pide un email y verifica si contiene "@" y termina en ".com" (usa in y el método .endswith()).
"""""""""
email = input("Digite un email: ") #Creamos la variable y le pedimos el correo al usuario
#creamos la condicio y lo imprimimos
if "@" in email and email.endswith(".com"):
    print(f"El email '{email}' tiene un fromato valido.")
else:
    print(f"El email '{email}' NO es válido. Debe contener '@' y terminar en '.com'.")
