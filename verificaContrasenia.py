import re
from colorama import Fore, Style, init

init(autoreset=True)

def verificarFortaleza(contrasenia):
    contador = 0

    if len(contrasenia) >= 8:
        contador += 1
    if re.search('[a-z]', contrasenia):
        contador += 1
    if re.search('[A-Z]', contrasenia):
        contador += 1
    if re.search('[0-9]', contrasenia):
        contador += 1
    if re.search('[@#/&!="·"·]', contrasenia):
        contador += 1

    return contador


def main():
    while True:    
        contrasenia = input('Introduce una contraseña: ')
        fortaleza = verificarFortaleza(contrasenia)

        if fortaleza == 5:
            print(Fore.GREEN + 'La contraseña es segura')
        elif fortaleza >= 3:
            print(Fore.YELLOW + 'La contraseña es medianamente segura')
        else:
            print(Fore.RED + 'La contraseña no es segura')
        
        if fortaleza < 3:
            print(Fore.RED + 'La contraseña debe tener al menos 8 caracteres, una mayúscula, una minúscula, un número y un caracter especial')
            continuar = input('¿Quieres intentarlo de nuevo? (s/n): ')
            if continuar != "s":
                print(Fore.CYAN + '¡Hasta luego!')
                break
        else:
            print(Fore.CYAN + 'Contraseña aceptada!')
            break

if __name__ == "__main__":
    main()