def segundoMasGrande(lista):

    numeroMasGrande = max(lista)

    for numero in lista:
        if numero == numeroMasGrande:
            lista.remove(numero)

    segundoMasGrande = max(lista)
    return 'El segundo número más grande es: ' + str(segundoMasGrande)

if __name__ == "__main__":
    lista = [1,3,5,2,7,45,2,98]
    print(segundoMasGrande(lista))