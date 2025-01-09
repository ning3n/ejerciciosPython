from math import tan, pi

def area_poligono_regular(n, s):
    """
    Calcula el área de un polígono regular.
    
    Parámetros:
    n (int): Número de lados del polígono.
    s (float): Longitud de cada lado del polígono.
    
    Retorna:
    float: Área del polígono regular.
    """

    area = n * s**2 / (4 * tan(pi/n))
    return area

numero_lados = 5
longitud_lados = 12
print(area_poligono_regular(numero_lados, longitud_lados))

