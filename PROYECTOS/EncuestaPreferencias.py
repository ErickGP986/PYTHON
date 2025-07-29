'''
Encuesta de preferencias

Simula una encuesta donde varios usuarios eligen sus lenguajes de programación favoritos.

Usa sets para:

Ver qué lenguajes se mencionaron.

Encontrar los lenguajes comunes entre todos.

Ver qué lenguajes eligieron unos pero no otros.
'''
# Lista para almacenar los lenguajes seleccionados por cada usuario
preferencias_usuarios = []

usuarios = int(input("¿Cuántos usuarios son?: "))

for i in range(usuarios):
    print(f"\nUsuario {i+1}:")
    print("Elige tu lenguaje de programación favorito:")
    print("1. C/C++")
    print("2. Python")
    print("3. Java")
    print("4. JavaScript")
    print("5. GO")
    print("6. PHP")
    
    lenguajes_usuario = set()  # Cada usuario puede tener múltiples preferencias
    
    while True:
        opcion = int(input("Elige tu opción (0 para terminar): "))
        
        if opcion == 0:
            break
        elif opcion == 1:
            lenguajes_usuario.add("C/C++")
        elif opcion == 2:
            lenguajes_usuario.add("Python")
        elif opcion == 3:
            lenguajes_usuario.add("Java")
        elif opcion == 4:
            lenguajes_usuario.add("JavaScript")
        elif opcion == 5:
            lenguajes_usuario.add("GO")
        elif opcion == 6:
            lenguajes_usuario.add("PHP")
        else:
            print("Opción no válida. Intenta nuevamente.")
    
    preferencias_usuarios.append(lenguajes_usuario)

# Análisis de resultados
if preferencias_usuarios:
    # 1. Todos los lenguajes mencionados
    todos_lenguajes = set()
    for lenguajes in preferencias_usuarios:
        todos_lenguajes.update(lenguajes)
    
    print("\nTodos los lenguajes mencionados:", todos_lenguajes)
    
    # 2. Lenguajes comunes a todos
    comunes = set(preferencias_usuarios[0])
    for lenguajes in preferencias_usuarios[1:]:
        comunes.intersection_update(lenguajes)
    
    print("Lenguajes comunes a todos:", comunes if comunes else "Ninguno")
    
    # 3. Conteo por lenguaje
    print("\nPreferencias por lenguaje:")
    for lenguaje in sorted(todos_lenguajes):
        contador = sum(1 for lenguajes in preferencias_usuarios if lenguaje in lenguajes)
        print(f"{lenguaje}: {contador} usuarios")
else:
    print("No se ingresaron datos de usuarios.")
