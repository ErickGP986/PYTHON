'''
Detector de duplicados en archivos

Dado un archivo de texto con un elemento por línea, muestra qué elementos están duplicados.

Tip: Puedes ir guardando en un set y comprobar si ya estaba.
'''
import string

try:
    texto = input("Ingrese un párrafo: ").strip()
    
    if not texto:
        print("Error: No ingresaste ningún texto")
    else:
        # Limpiar signos de puntuación y separar palabras
        palabras = [
            palabra.strip(string.punctuation)
            for palabra in texto.lower().split()
            if palabra.strip(string.punctuation)
        ]
        
        palabras_unicas = sorted(set(palabras))  # Ordenadas alfabéticamente
        
        # Escribir en archivo
        with open('palabra.txt', 'w', encoding='utf-8') as archivo:
            archivo.write(texto)
        
        # Mostrar resultados
        print(f"\nTexto ingresado: {texto}")
        print(f"\nPalabras únicas ({len(palabras_unicas)}):")
        for i, palabra in enumerate(palabras_unicas, 1):
            print(f"{i}. {palabra}")
            
except Exception as e:
    print(f"Ocurrió un error: {e}")




