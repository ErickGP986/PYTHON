'''
Diferencia

Calcula qué elementos están en s1 pero no en s2.
'''
s1 =  {1, 2, 3} #creamos el primer set
s2 = {3, 4, 5} #creamos el segundo set

dos_set = s1.difference(s2) #unimos los dos set

print(f"El primer set es: {s1}") #imprimimos el primer set
print(f"El segundo set es: {s2}") #imprimimmos le segundo set
print(f"La diferencia de los set es: {dos_set}") #imprimimmos la diferencia
