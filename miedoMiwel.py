# Programa que recibe una cadena de texto y retorna la cadena de texto invertida sin usar la funcion reverse.

def invertirCadena(cadena):
    cadenaInvertida = ''
    for i in range(len(cadena)-1, -1, -1): # Recorremos la cadena de texto de atras hacia adelante
        cadenaInvertida += cadena[i]
    return cadenaInvertida

if __name__ == '__main__':
    cadena = input('Introduce una cadena de texto: ')
    print(invertirCadena(cadena))