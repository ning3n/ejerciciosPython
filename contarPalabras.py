#cuenta palabras

cadenaPalabras = 'it was the best of times it was the worst of times '
cadenaPalabras += 'it was the age of wisdom it was the age of foolishness'
listaPalabras = cadenaPalabras.split()

frecuenciaPalab = [listaPalabras.count(w) for w in listaPalabras] #cuenta las palabras

print("Cadena\n" + cadenaPalabras +"\n")
print("Lista\n" + str(listaPalabras) + "\n")
print("Frecuencias\n" + str(frecuenciaPalab) + "\n")
print("Pares\n" + str(list(zip(listaPalabras, frecuenciaPalab)))) #imprime las palabras y su frecuencia