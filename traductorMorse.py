MORSE = {' ': '_', 'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', }

def convertirAMorse(frase):
    frase = frase.upper()
    fraseCodificada = ""
    for letra in frase:
        fraseCodificada += MORSE[letra] + " "
    return fraseCodificada

frase = input("Introduce una frase: ")
fraseCodificada = convertirAMorse(frase)
print(fraseCodificada)  # Imprime la frase codificada en morse