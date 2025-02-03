
class numerosDesordenados(Exception):
    pass

class numerosRepetidos(Exception):
    pass

def validacion(listaNumeros):
    contadorNumeros = 0

    try:
        for numero in listaNumeros:
            contadorNumeros = ListaNumeros.count(numero)
            if contadorNumeros > 1:
                raise numerosRepetidos
            else:
                contadorNumeros = 0
                continue

        for numero in listaNumeros:
            if numero > listaNumeros[-1]:
                raise numerosDesordenados
            
    except numerosDesordenados:
        print('Los números están desordenados')
        return False
    except numerosRepetidos:
        print('Hay números repetidos')
        return False
    else:
        print('El argumento es valido!')
        return True

def numerosPerdidos(listaNumeros):
    comprobacion = validacion(listaNumeros)
    if comprobacion == False::
        return 'corrige y vuelve a intentarlo'
    elif comprobacion == True:

        numerosDentro = list(range(listaNumeros[0], listaNumeros[-1]))

        for numero in listaNumeros:
            if numero in numerosDentro:
                numerosDentro.remove(numero)

        else:
            if len(numerosDentro) == 0:
                return 'La lista-argumento contiene todos los numeros entre el {} y el {}.format(listaNumeros[0], listaNumeros[-1])'
            else:
                print('los numeros perdidos son: ')
                return numerosDentro

if __name__ == "__main__":
    print(numerosPerdidos([1,2,5,5,7,8]))