# Crea un programa que calcule quien gana mas partidas al
# piedra papel tijeras
# - El resultado puede ser: "Player1", "Player2" o "Empate"
# - La funcion recibe un listado que contiene pares, representando cada jugada.
# - El par puede contener combinaciones de "R" (piedra), "P"(papel) o "S"(tijeras)
# - Ejemplo Entrada: [("R", "S"), ("S", "R"), ("P", "S")]. Resultado: "Player2"
#

# Pîedra = 'R'
# Papel = 'P'
# Tijeras = 'S'

def quienGana(lista):
    """Funcion que recibe una lista de tuplas con las jugadas de dos jugadores y devuelve el ganador de la partida.
    
       Parametros:
       - lista : Lista que contiene una serie de tuplas con las jugadas de dos jugadores.
       
       La funcion recorre la lista de tuplas y compara los elementos de cada tupla para determinar el ganador.
       En caso de empate, se imprime por pantalla un mensaje informando de ello.
    """
    try:
        assert type(lista) == list
        for jugada in lista:
            if jugada[0] == 'R' and jugada[1] == 'S':
                print('Player1 gana')
            elif jugada[0] == 'S' and jugada[1] == 'R':
                print('Player2 gana')
            elif jugada[0] == 'R' and jugada[1] == 'P':
                print('Player2 gana')
            elif jugada[0] == 'P' and jugada[1] == 'R':
                print('Player1 gana')
            elif jugada[0] == 'P' and jugada[1] == 'S':
                print('Player2 gana')
            elif jugada[0] == 'S' and jugada[1] == 'P':
                print('Player1 gana')
            else:
                print('Empate')
    except AssertionError:
        print('El valor introducido no es valido. Introduzca una lista de tuplas con las jugadas de dos jugadores.')