#/*
#* Crea una función que evalúe si un/a atleta ha superado correctamente una
#* carrera de obstáculos.
#* - La función recibirá dos parámetros:
#*      - Un array que sólo puede contener String con las palabras
#*        "run" o "jump"
#*      - Un String que represente la pista y sólo puede contener "_" (suelo)
#*        o "|" (valla)
#* - La función imprimirá cómo ha finalizado la carrera:
#*      - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla)
#*        será correcto y no variará el símbolo de esa parte de la pista.
#*      - Si hace "jump" en "_" (suelo), se variará la pista por "x".
#*      - Si hace "run" en "|" (valla), se variará la pista por "/".
#* - La función retornará un Boolean que indique si ha superado la carrera.
#* Para ello tiene que realizar la opción correcta en cada tramo de la pista.
#*/

def carrera(array, str):

    try:
        assert len(array) == len(str)
        listaStringPistaFinal = [] #inicializamos una lista que contendra los elementos que vayamos imprimiendo en pantalla
        contador = 0 #a lo largo de la carrera, y una variable contador que usaremos para referirnos al indice.
        for accion in array:
            if accion != 'run' and accion != 'jump':
                print(' ', end='\n')
                raise Exception('El array solo puede contener "run" o "jump"')

            elif accion == 'run' and str[contador] == '_': #Ejecutamos un bucle para iterar sobre los elementos del array argumento
                print('_', end='') #Si el atleta corre en el suelo, se imprime un guion bajo
                listaStringPistaFinal.append('_')
                contador += 1 #incrementamos el contador para pasar al siguiente elemento del array argumento	
            elif accion == 'jump' and str[contador] == '|': #Si el atleta salta una valla, se imprime una barra vertical
                print('|', end='')
                listaStringPistaFinal.append('|')
                contador += 1
            elif accion == 'run' and str[contador] == '|':
                print('/', end='') #Si el atleta corre en el suelo, se imprime un guion bajo
                listaStringPistaFinal.append('/')
                contador += 1
            elif accion == 'jump' and str[contador] == '_': #Si el atleta salta una valla, se imprime una barra vertical
                print('x', end='')
                listaStringPistaFinal.append('x')
                contador += 1
        
        for item in listaStringPistaFinal:
            if item != '_' or item != '|':
                print('', end='\n')
                return false
            else:
                print('', end='\n')
                True
    except AssertionError:
        if len(array) > len(str):
            print('La pista es demasiado corta para la cantidad de acciones asignadas al atleta.')
        elif len(array) < len(str):
            print('La pista es demasiado larga para la cantidad de acciones asignadas al atleta.')
        else:
            print('Ha ocurrido un error al especificar el array de acciones o el string de la pista.')
    except Exception:
        print('Ha ocurrido un error al especificar el array de acciones o el string de la pista.')
    