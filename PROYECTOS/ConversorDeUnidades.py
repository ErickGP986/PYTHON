"""""
2. Conversor de Unidades (Intermedio)
Descripción: Convierte entre diferentes unidades (temperatura, longitud, peso, etc.).
Habilidades usadas:

Condicionales (if-elif-else).

Funciones matemáticas (fórmulas de conversión).
Opciones a incluir:

Celsius ↔ Fahrenheit.

Kilómetros ↔ Millas.

Kilogramos ↔ Libras.
"""""""""
while True: #Creamos un bucle para que se quede repitiendo
 print("\tElige la conversion.") #le damos el menu
 print("\t1. Celcius a Fahrenheit.")
 print("\t2. farenheit a celcius.")
 print("\t3. Kilometros a millas.")
 print("\t4. millas a Kilometros.")
 print("\t5. Kilogramos a libras.")
 print("\t6. Libras a kilogramos.")
 print("\t7. Salir")
 opcion = int(input("¿Que opcion elige?: ")) #Le pedimos que opcion quiere

 if(opcion == 1): #Creamos la opcion 1 y hacemos los calculos
    celcius = float(input("Ingrese los grados celcius: "))
    fahrenheits = (celcius * 9/5) + 32
    print(f"Los celcius: {celcius} convertido a fahrenheit es: {round(fahrenheits, 2)}")
 elif(opcion == 2): #Creamos la segunda opcion haciendo los calculos
    fahrenheits = float(input("ingrese los gardos en fahrenheits: "))
    celcius = (fahrenheits - 32) * 5/9
    print(f"Los fahrenheits: {fahrenheits} convertido a celcius es: {round(celcius, 2)}")
 elif(opcion == 3): #Creamos la tercera opcion
    kilometros = float(input("Ingrese cuantos kilometros son: "))
    millas = kilometros * 0.621371
    print(f"Los kilometros: {kilometros} convertidos a millas es: {round(millas, 2)}")
 elif(opcion == 4): #Creamos la cuarta opcion
    millas = float(input("Ingrese cuanto son las millas: "))
    kilometros = millas * 1.60934
    print(f"Las millas: {millas} convertido a kilometros es: {round(kilometros, 2)}")
 elif(opcion == 5): #Creamos la quinta opcion 
    kilogramos = float(input("Ingrese cuantos kilogramos son: "))
    libras = kilogramos * 2.20462
    print(f"Los kilogramos {kilogramos} convertidos a Libras son: {round(libras, 2)}")
 elif(opcion == 6): #Creamos la sexta opcion
    libras = float(input("Ingrese cuantas libras son: "))
    kilogramos = libras * 0.453592
    print(f"La libras: {libras} convertido a kilogramos es: {round(kilogramos, 2)}")
 elif(opcion == 7): #Creamos la 7 opcion
    print("Hasta luego.")
    break
 else: #y si el usuario no elige esa opcion le decimos que eliga una
    print("Usted no digito alguna de esas opciones.. por favor vuelvealo intentar.")
    
