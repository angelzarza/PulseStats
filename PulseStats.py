"""ANGEL ZARZA OLIVARES"""

import os
import sys
from pynput import keyboard as kb
from pynput.mouse import Listener

"""Creamos los archivos en el directorio raíz del script"""
FILE_NAME = "log.txt"
f = open(FILE_NAME, "a+")


def default_file():
    """Leemos el archivo, si contiene información no sucede nada, pero si esta vacío, crea por defecto una línea
    de texto con el número 0."""
    f = open(FILE_NAME, "r")
    line = f.readline()
    print(line)

    if os.stat("log.txt").st_size == 0:
        f = open(FILE_NAME, "w+")
        #f.write("0\n0")
        f.write("0")


def clear_file():
    """Función que limpia el fichero."""
    while True:
        if os.path.isfile(FILE_NAME):  # isfile comprueba si existe el fichero
            verify = str(input("Desea vaciar el fichero " + FILE_NAME + " (S/N)? "))
            if verify == "N" or verify == "n":
                print("OK")
                break
            elif verify == "S" or verify == "s":
                f = open('log.txt', 'w')
                print("El fichero se ha vaciado.")
                break
            elif verify.isdigit():  # Comprobamos que no sean números
                print("Carácter no válido.")
                continue
            else:
                print("Carácter no válido.")
                continue

    print("Se ha completado con éxito.")


def close_file():
    """Función para cerrar el fichero"""
    f.close()


def save_key(key):
    """Variables que almacenan datos temporalmente para trabajar con ellos.
    Parámetros:
        buffer_1 guarda el valor de log.txt y buffer_2 por defecto sera siempre 1"""
    buffer_1 = []
    buffer_2 = [1]

    """Abrimos el archivo en modo lectura, leemos su contenido y los convertimos a un entero que se guardara 
    en el buffer_1. Por ultimo sumamos ambos buffer y guardamos el resultado en una variable.
        Parámetros: 
            result: Guarda la suma de buffer_1 y buffer_2 en la variable, siempre que tengan ambos la 
            misma longitud."""
    f = open(FILE_NAME, "r")
    line = int(f.readline())
    buffer_1.append(line)
    result = [buffer_1[i] + buffer_2[i] for i in range(len(buffer_1))]

    """Hacemos una conversión de list a str y eliminamos caracteres para limpiar el resultado."""
    convert = str(result)
    save = convert.strip("[]")

    """Guarda el registro en el fichero, eliminando el anterior contenido que tenia."""
    f = open(FILE_NAME, "w+")
    f.write(str(save))

    print('Se ha pulsado la tecla ' + str(key))


def on_click(x, y, button, pressed):
    if pressed:
        """Variables que almacenan datos temporalmente para trabajar con ellos.
            Parámetros:
                buffer_1 guarda el valor de log.txt y buffer_2 por defecto sera siempre 1"""
        buffer_1 = []
        buffer_2 = [1]

        """Abrimos el archivo en modo lectura, leemos su contenido y los convertimos a un entero que se guardara 
        en el buffer_1. Por ultimo sumamos ambos buffer y guardamos el resultado en una variable.
            Parámetros: 
                result: Guarda la suma de buffer_1 y buffer_2 en la variable, siempre que tengan ambos la 
                misma longitud."""
        f = open(FILE_NAME, "r")
        line = int(f.readline())
        buffer_1.append(line)
        result = [buffer_1[i] + buffer_2[i] for i in range(len(buffer_1))]

        """Hacemos una conversión de list a str y eliminamos caracteres para limpiar el resultado."""
        convert = str(result)
        save = convert.strip("[]")

        """Guarda el registro en el fichero, eliminando el anterior contenido que tenia."""
        f = open(FILE_NAME, "w+")
        f.write(str(save))

        print("Presionado: ", pressed)
    else:
        # print("CLick es false, no se ejecuta nada")
        pass


def exceptions():
    """Controla los posibles errores generados al ejecutar o al salir del programa."""
    with kb.Listener(save_key), Listener(on_click=on_click) as event:
        try:
            event.join()
        except KeyboardInterrupt:
            print("Finalizo correctamente.")
            close_file()
            sys.exit()


def main():
    """Función principal que ejecuta las demás funciones del código."""
    clear_file()
    default_file()
    exceptions()


if __name__ == "__main__":
    main()
