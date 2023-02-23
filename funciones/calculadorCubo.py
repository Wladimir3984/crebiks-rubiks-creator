import numpy as np

def calcularPiezas(lado_a, lado_b, lado_c):
   if es_cuadrado(lado_a, lado_b, lado_c): #calcular cara 
       cara = cara_cuadrado(lado_a)
       sup_inf = sup_inf_cuadrado(cara)
       aristas_centrales = aristas_centrales_cuadrado(cara,lado_a)
       centro = centro_cuadrado(cara,lado_a)
       total = sup_inf + aristas_centrales+(centro*2)

       return [total,cara,sup_inf,aristas_centrales,centro] #retorna datos necesarios para armar el cubo en 3D
   else:
       return False # calcular por partes el cubo solo si es rectangular, todavia no disponible

def es_cuadrado(a,b,c):
    if a==b==c:
        return True
    return False

# calcular por partes el cubo solo si es de partes cuadradas
def cara_cuadrado(lado):
    return lado*lado
def sup_inf_cuadrado(cara):
    return cara*2
def aristas_centrales_cuadrado(cara,lado):
    return (cara - (lado*2)) * 2
def centro_cuadrado(cara,lado):
    return int(np.sqrt(cara - (lado*2)))**2





