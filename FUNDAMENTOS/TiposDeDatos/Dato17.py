"""""
¿Qué tipo es?
Pide al usuario que ingrese un valor y determina su tipo con type().
Ejemplo:
valor = input("Ingresa un valor: ")  
# Intenta convertirlo a int, float o déjalo como string  
"""""""""
valor = input("Ingresa un valor: ")

# Intentar determinar el tipo
try:
    # Primero intentamos convertirlo a entero
    valor_convertido = int(valor)
    tipo = "entero (int)"
except ValueError:
    try:
        # Si no es entero, intentamos convertirlo a decimal
        valor_convertido = float(valor)
        tipo = "decimal (float)"
    except ValueError:
        # Si no es numérico, lo dejamos como string
        valor_convertido = valor
        tipo = "texto (str)"

# Mostrar el resultado
print(f"El valor '{valor_convertido}' es de tipo: {tipo}")
