"""""
1. Calculadora de Propinas (Básico)
Descripción: Un programa que calcule el monto total a pagar en un restaurante, incluyendo propina.
Habilidades usadas:

Input/output (input(), print()).

Operaciones matemáticas (suma, multiplicación).

Variables y tipos de datos (float, int).
Extras:

Permite al usuario elegir el porcentaje de propina (10%, 15%, 20%).

Redondea el resultado a 2 decimales.
"""""""""

total_cuenta = int(input("Digite el total de la cuenta: ")) #Aqui le pedimos al usuario que igrese el monto de la cuenta

propina = input("Desea dejar propina (s/n): ") #Aqui preguntamos si quiere dejar propina
#Si, si quiere dejar propina hacemos los calculos 
if(propina == "s"):
    cuanto = int(input("Cuanto desea dejar (10%), (15%) y 20%: ")) #Le decimos si quiere un 10 , 15 o 20
    subtotal = float(cuanto * total_cuenta) /100 #hacemos los calculos de la propina
    total_pagar = float(subtotal + total_cuenta) #Hacemos el total a pagar
else: #si no, simplemente dejamos la cuenta cerrada
    print("Usted ah decidido no dejar propina.")
    total_pagar = float(total_cuenta)
    subtotal = 0
#Lo imprimimos
print(f"Propina: ${subtotal} | Total a pagar: ${total_pagar}")

