# Crear un programa que dibuje un cuadrado o un triangulo con asteriscos
# Indicaremos el tamaño del lado y si la figura a dibujar es una u otra
#

def dibujo():
    #Funcion sin parametros que hace una serie de preguntas relacionadas con la formacion de una
    #figura geometrica e imprime finalmente la figura por pantalla.
    #Esta figura es diferente en funcion de que respuestas se le han ido proporcionando a lo largo del transcurso del programa.

    figura = int(input('''Selecciona la figura que deseas mostrar:
            1. Cuadrado(seleccione '1')    
            2. Triangulo(seleccione '2')
            '''))

    if figura == 1:
        medida = int(input("Escriba la longitud del lado del cuadrado: "))
        if medida > 250:
            for i in range(medida):
                print('* ' * medida)
                resto = medida % 3
                for num in range((medida//2) + resto):
                    print('*','*',sep=' '*(medida-2))
                
                print('* ' * medida)
        elif medida >= 10:
            print('* ' * medida)
            resto = medida % 3
            for num in range((medida//3) + resto):
                print('*','*',sep=' '*(medida-2))

            print('* ' * medida)
        elif medida == 8:
            print('*' * medida)
            for num in range((medida//3) + 1):
                print('*','*',sep=' '*(medida-2))
            
            print('*' * medida)
        elif medida < 10:
            print('*' * medida)
            for num in range(medida//3):
                print('*','*',sep=' '*(medida-2))
            
            print('*' * medida)
    
    elif figura == 2:
        base = int(input('Introduzca un valor para la base del triangulo: '))
        altura = int(input('Introduzca un valor para la altura del triangulo: '))
        try:
            assert (base > altura) and (base > 0) and (altura > 0)
            print('*')
            for num in range(altura):
                print('*','*',sep=' ' * num)

            else:
                if base >= 20 and altura <= 10:
                    base -= 8
            print('*' * base)
            print('Ha sido necesario ajustar la longitud de la base del triangulo para que se pueda visualizar correctamente.')
        except AssertionError:
            print('El valor introducido no es valido. Introduzca un valor para la base mayor que la altura y mayor que 0.')

if __name__=='__main__':
    dibujo()