'''
Edad para votar:
Pide la edad del usuario y muestra True si puede votar (edad ≥ 18).

python
edad = int(input("Edad: "))
print(edad >= 18)
'''
edad = int(input("Ingrese tu edad: ")) #Le pedimos la edad al usuario

if(edad >= 18): #creamos la condicion de si es mayor o igual al 18
    print("Si puede votar.") #si es verdad puede votar
else:
    print("Usted no puede votar.") #Si es falso no puede votar
