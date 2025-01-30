# Simula el funcionamiento de una maquina expendedora creando una operacion
# que reciba dinero (array de monedas) y un numero que indique la seleccion
#del producto.
#El programa retornara el nombre del producto y un array con el dinero
# de vuelta (con el menor numero de monedas)
# Si el dinero es insuficiente o el numero de producto no existe,
# debera indicarse con un mensaje y retornar todas las monedas.
# Si no hay dinero de vuelta, el array se retornara vacio
# Para que resulte mas simple, trabajaremos en centimos con monedas de
# 5, 10, 50, 100 y 200
# Debemos controlar que las monedas enviadas esten dentro de las soportadas

import time

class BotellaAgua():
    nombre = 'Botella de Agua'
    precio = 80
    nProducto = 1

class BolsaPapas():
    Nombre = 'Bolsa de Papas'
    precio = 120
    nProducto = 2

class Golosina():
    nombre = 'Golosina'
    precio = 100
    nProducto = 3

def maquinaExpendedora(listaMonedas):
    #Funcion que actua como maquina expendedora
    # Parametros:
    # listaMonedas: es una lista de enteros que el usuario debe pasar como argumento al momento de invocarla funcion.
    #               En funcion de los enteros que compongan la lista, y del producto que haya seleccionado para comprar
    #               la funcion tomara un camino u otro, imprimiendo por pantalla un resultado u otro.
    monedasPermitidas = [5, 10, 50, 100, 200]
    botellaAgua = BotellaAgua()
    bolsaPapas = BolsaPapas()
    golosina = Golosina()

    for moneda in listaMonedas:
        if moneda in monedasPermitidas:
            continue
        else:
            print('Se ha introducido una moneda no permitida')
            return listaMonedas

    try:
        producto = int(input("""Introduce el numero del producto que deseas comprar: 
        1. Botella de Agua
        2. Bolsa de Papas
        3. Golosina
        """))
        assert producto > 0 and producto < 4

        total_dinero_introducido = sum(listaMonedas)

        if producto == 1:
            if botellaAgua.precio > total_dinero_introducido:
                print('Dinero insuficiente')
                time.sleep(1)
                print('Se han devuelto {} centimos.'.format(total_dinero_introducido))
                return
            elif botellaAgua.precio == total_dinero_introducido:
                print('Entregando su producto')
                time.sleep(2)
                print('Producto comprado: {}'.format(botellaAgua.nombre))
                return
            else:
                print('Entregando su producto')
                time.sleep(2)
                print('Producto comprado: {}'.format(botellaAgua.nombre))
                dineroSobrante = total_dinero_introducido - botellaAgua.precio
                print('Te han sobrado {} centimos...'.format(dineroSobrante))

        if producto == 2:
            if bolsaPapas.precio > total_dinero_introducido:
                print('Dinero insuficiente')
                time.sleep(1)
                print('Se han devuelto {} centimos.'.format(total_dinero_introducido))
                return
            elif bolsaPapas.precio == total_dinero_introducido:
                print('Entregando su producto')
                time.sleep(2)
                print('Producto comprado: {}'.format(bolsaPapas.nombre))
                return
            else:
                print('Entregando su producto')
                time.sleep(2)
                print('Producto comprado: {}'.format(bolsaPapas.nombre))
                dineroSobrante = total_dinero_introducido - bolsaPapas.precio
                print('Te han sobrado {} centimos...'.format(dineroSobrante))

        if producto == 3:
            if golosina.precio > total_dinero_introducido:
                print('Dinero insuficiente')
                time.sleep(1)
                print('Se han devuelto {} centimos.'.format(total_dinero_introducido))
                return
            elif golosina.precio == total_dinero_introducido:
                print('Entregando su producto')
                time.sleep(2)
                print('Producto comprado: {}'.format(golosina.nombre))
                return
            else:
                print('Entregando su producto')
                time.sleep(2)
                print('Producto comprado: {}'.format(golosina.nombre))
                dineroSobrante = total_dinero_introducido - golosina.precio
                print('Te han sobrado {} centimos...'.format(dineroSobrante))


    except AssertionError:
        print('El producto seleccionado no existe')
        print('Devolviendo monedas...')
        return listaMonedas

if __name__ == '__main__':
    maquinaExpendedora([10, 100])