'''
Subset y superset

Comprueba si {1,2} es subconjunto de {1,2,3}.

Comprueba si {1,2,3} es un superset de {2}.
'''
s1 = {1, 2} #creamos el primer set
s2 = {1, 2, 3} #creamos el segundo set

subconjunto = s1.issubset(s2) #creamos el subconjunto
superset = s2.issuperset(s1) #creamos el superset

print(f"El primer set es: {s1}") #imprimimos el primer conjunto
print(f"El segundo set es: {s2}") #imprimimos el segundo conjunto
print(f"El subconjunto del primer al segundo conjunto es: {subconjunto}") #imprimimmos el subconjunto
print(f"El superset es: {superset}") #imprimimos el superset
