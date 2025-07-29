'''
Gestor de contactos sin duplicados

Crea una aplicación que almacene nombres en un set.

Permite agregar, eliminar, y mostrar contactos sin duplicados.
'''
contactos = set() #creamos el set

while True: #creamos un bucle while para que se repita
    #mostramos las opciones que puede hacer
    print("\n--- Agenda de Contactos ---")
    print("0. Salir")
    print("1. Añadir contacto")
    print("2. Eliminar contacto")
    print("3. Mostrar contactos")
    #creamos un try-except para que tenga que si o si introduir un numero
    try:
        opcion = int(input("Ingrese la opción que desee: ")) #le pedimos la opcion al usuario
    except ValueError:
        print("Error: Por favor ingrese un número válido.") #imprimimos que introduzca el numero
        continue #y que continue

    if opcion == 0: #creamos la opcion 0 que es para terminar el programa
        print("Saliendo del programa...")
        break #lo terminamos
        
    elif opcion == 1: #creamos la opcion 1 que es para añadir los contactos
        usuario = input("Qué contacto quiere agregar: ").strip() #le pedims al usuario que desea agregar
        if usuario in contactos: #vemos si el usuario ya existe
            print(f"Error: El contacto '{usuario}' ya existe.") #y si, si le decimos que ya esta agregado
        else: #si no
            contactos.add(usuario) #el contacto si se agrega correctamente
            print(f"Contacto '{usuario}' agregado exitosamente.") #le decimos que el contacto se agrego correctamente
            
    elif opcion == 2: #creamos la 2 opcion que es quitar al contacto
        usuario = input("Qué contacto desea eliminar: ").strip() #igual le pedimos al usuario el contacto que desea quitar
        if usuario in contactos: #vemos si el usuario ya esta registrado
            contactos.remove(usuario) #si, si se puede remover
            print(f"Contacto '{usuario}' eliminado exitosamente.") #y decimos que el contacto se removio correctamente
        else: #si no existe el contacto
            print(f"Error: El contacto '{usuario}' no existe.") #le decimos que no se puede porque no existe
            
    elif opcion == 3: #creamos la opcion 3 de mostrar los contactos
        if contactos: #vemos los elementos del set contactos
            print("\n--- Lista de Contactos ---") #le decimos su lista de contactos
            for i, contacto in enumerate(sorted(contactos), 1): #creamos el bucle que desempaquetamos los contactos, los enumeramos y los ordenamos alfabeticamente
                print(f"{i}. {contacto}") #mostramos los contactos
        else: #y si no
            print("No hay contactos registrados.") #le decimos que no hay contactos registrados
            
    else: #si el usuario no ingresa esa opciones le decimos que escoga una de las 4
        print("Opción no válida. Por favor ingrese 0, 1, 2 o 3.")
