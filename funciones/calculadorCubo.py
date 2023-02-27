def calcularPiezas(lado_a, lado_b, lado_c):
    cubo = str(lado_a) + "x" + str(lado_b) + "x" + str(lado_c)
    if lado_a == 1 and lado_b == 1 and lado_c == 1:  # 1x1x1
        return {"cubo": cubo,
                "piezas": 1,
                "front_plus_back": 0,
                "aristas_centrales": 0,
                "centro_left_plus_right": 0,
                "centro_up_plus_down": 0}
    if tiene_dos_profundidad(lado_a, lado_b, lado_c):
        return dos_dimensiones_resultado(lado_a, lado_b, lado_c, cubo)

    cara = cara_cuadrado(lado_a, lado_b)
    sup_inf = sup_inf_cuadrado(cara)
    aristas_centrales = aristas_centrales_cuadrado(cara, lado_a, lado_b)
    centro = (centro_cuadrado(cara, lado_a, lado_b))
    centro_rect = 0

    # si es rectangular se calcula los dos centros que son diferentes de las otras caras
    if is_rectangular(lado_a, lado_b, lado_c):
        centro *= 2
        centro_rect = (centro_rectangular(lado_b, lado_c))*2

    else:
        centro *= 4

    total = sup_inf + aristas_centrales+(centro + centro_rect)
    return {"cubo": cubo,
            "piezas": total,
            "front_plus_back": sup_inf,
            "aristas_centrales": aristas_centrales,
            "centro_left_plus_right": centro,
            "centro_up_plus_down": centro_rect}

# si tiene dos profundidad


def tiene_dos_profundidad(lado_a, lado_b, lado_c):
    if lado_a == 2 or lado_b == 2 or lado_c == 2:
        return True
    return False


def dos_dimensiones_resultado(lado_a, lado_b, lado_c, cubo):
    cara = 0
    sup_inf = 0
    if lado_a == 2:
        cara = lado_b*lado_c
        sup_inf = cara*2
    elif lado_b == 2:
        cara = lado_a*lado_c
        sup_inf = cara*2
    elif lado_c == 2:
        cara = lado_a*lado_b
        sup_inf = cara*2
    return {"cubo": cubo,
            "piezas": sup_inf,
            "front_plus_back": sup_inf,
            "aristas_centrales": 0,
            "centro_left_plus_right": 0,
            "centro_up_plus_down": 0}


# calcular por partes el cubo solo si es de partes cuadradas
def cara_cuadrado(alto, ancho):
    return alto*ancho


def sup_inf_cuadrado(cara):
    return cara*2


def aristas_centrales_cuadrado(cara, alto, ancho):
    return ((cara - (alto*2)) - centro_cuadrado(cara, alto, ancho))*2


def centro_cuadrado(cara, alto, ancho):
    return (cara-(alto*2)) - ((ancho-2)*2)

# calculo para cubo rectangular


def is_rectangular(lado_a, lado_b, lado_c):
    if lado_a != lado_b or lado_a != lado_c or lado_b != lado_a or lado_b != lado_c or lado_c != lado_a or lado_c != lado_b:
        return True
    return False


def centro_rectangular(ancho, profundidad):
    cara = ancho * profundidad
    return (cara - (ancho*2)) - ((profundidad-2)*2)
