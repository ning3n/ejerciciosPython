# Crea una funcion que reciba un texto y muestre cada palabra en una linea
# formando un marco rectangular de asteriscos
# ¿Que te parece el reto? se veria asi:
# ********
#*   * ¿Qué   *
#*   * te     *
#*   * parece *
#*   * el     *
#*   * reto?  *
#*   **********

def marco_palabras(texto):
    texto = input("Introduce el texto a enmarcar")

    listaPalabras = texto.split()
    listaLongitudes = []

    for palabra in listaPalabras:
        listaLongitudes.append(len(palabra))

    palabraMasLarga = max(listaLongitudes)

    separador = '*'*(palabraMasLarga+4)
    print(separador)
    for palabras in listaPalabras:
        string = '*' + ' ' + palabras +(' '*(len(separador) - len(palabras) - 3)) + '*'
        print(string)

    else:
        print(separador)

if __name__ == "__main__":
    marco_palabras()