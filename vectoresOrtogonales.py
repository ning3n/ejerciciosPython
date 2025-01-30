#Crea un programa que determine si dos vectores son ortogonales
# los dos array deben tener la misma longitud
# cada vector se podria representar como un array. Ejemplo: [1, -2]

def ortogonal(vector1,vector2):
    #Funcion que recibe dos vectores y determina si son ortogonales o no.
    #Para ello, se calcula el producto escalar de los dos vectores y se comprueba si el resultado es 0.
    #En caso de ser 0, los vectores son ortogonales, en caso contrario, no lo son.
    #Recibe dos parametros, vector1 y vector2, que son listas de numeros enteros.
    #Devuelve un valor booleano, True si son ortogonales, False en caso contrario.
    producto = 0
    for i in range(len(vector1)):
        producto += vector1[i] * vector2[i]
    if producto == 0:
        return True
    else:
        return False

if __name__=='__main__':
    vector1 = [1, 2]
    vector2 = [2, -1]
    print(ortogonal(vector1,vector2))