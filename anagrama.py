def anagrama(palabra1, palabra2):
    #Se convierten las cadenas a minusculas
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    #Las cadenas se convierten en arrays para reordenarlas, ya que asi es mas sencillo
    palabra1_arreglo = list(palabra1)
    palabra2_arreglo = list(palabra2)
    # se ordena el arreglo
    palabra1_arreglo.sort()
    palabra2_arreglo.sort()
    # Convertir de vuelta los arreglos a cadenas
    palabra1_ordenada = "".join(palabra1_arreglo)
    palabra2_ordenada = "".join(palabra2_arreglo)
    # Y finalmente comprobar si son iguales
    return palabra1_ordenada == palabra2_ordenada

cadena1 = input("Ingresa la primera palabra\n")
cadena2 = input("Ingresa la segunda palabra\n")
es_anagrama = anagrama(cadena1, cadena2)

if es_anagrama:
    print(f"{cadena1} es anagrama de {cadena2}")
else:
    print(f"{cadena1} NO es anagrama de {cadena2}")



    