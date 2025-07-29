'''
Acceso con usuario y contraseña:
Simula un login donde el usuario debe ingresar:

Usuario: "admin"

Contraseña: "1234"
Muestra True si ambos son correctos.

python
usuario = input("Usuario: ")
password = input("Contraseña: ")
print(usuario == "admin" and password == "1234")
'''
usuario_real = "admin" #creamos una variable que guarde el usuario verdadero
contraseña1 = "1234" #creamos la contraseña y la guardamos

usuario = input("Ingrese su usuario: ") #le pedimos el usuario
contraseña2 = input("Ingrese su contraseña: ") #Le pedimo la contraseña

if(usuario == usuario_real and contraseña1 == contraseña2): #creamos la condicion
    print("Pudiste entrar con exito.") #Le decimo que puedo acceder con exito
else:
    print("El usuario o contraseña esta mal vuelvelo a intentar.") #si no, que verifiqe su usuario o su contraseña
