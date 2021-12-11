import os.path
import time
import sys
from Ex1_Conversion import E1
from Ex2_Video_Comparison import E2
from Ex3_Live_Streaming import E3
#from Ex4_IP_Broadcast import E4

def s3_main(name):

    print("A continuación te mostraremos el listado de ejercicios disponibles en este lab:")
    print(f"....................................")
    print(f". 1. VP8, VP9, H.265 y AV1 codecs: .")
    print(f". 2. Comparación codecs video:     .")
    print(f". 3. Live Streaming:               .")
    print(f". 4. IP Broadcasting:              .")
    print(f".                                  .")
    print(f". 5. Salir del programa:           .")
    print(f"....................................")
    ex = input("¿Que ejercicio quieres ejecutar...?")
    if ex == '5':
        option = input(f"Estas seguro que desea salir del programa? \U0001F97A [y/n]")
        if option == 'y':
            sys.exit()
        else:
            s3_main(name)
    else:
        aux = 0
        while aux == 0:
            if ex == '1':
                self1 = E1()
                E1.main(self1, name)
            elif ex == '2':
                self2 = E2()
                E2.main(self2, name)
            elif ex == '3':
                self3 = E3()
                E3.main(self3, name)
            elif ex == '4':
                import Ex4
                Ex4.main()
            else:
                time.sleep(1)
                print(
                    "\nNúmero de ejercicio incorrecto \U00002620. Introduce uno de las 5 opciones disponibles:')\n")
                return

def test_material(defaultName):
    print(
        f"Primero de todo, necesitamos el nombre completo (nombre+extensió) de un archivo raíz al que se le aplicarán todas las modificaciones según los ejercicios.")
    time.sleep(1)
    print(
        f"En nuestro caso, el nombre de nuestro archivo es 'Resistencia_BM19.mp4' y este se encuentra en la carpeta media/, pero usted (si lo desea) puede utilizar uno propio.")
    print(
        f"Desea utilizar un archivo propio o, por el contrario, quiere utilizar el archivo por defecto 'Resistencia_BM19.mp4'?")
    print(f"[y: propio, n: por defecto]")
    resp = input()
    if resp == 'y':
        print(f"Primero, arrastre o copie el archivo a la carpeta media/")
        aux = False
        while aux == False:
            time.sleep(2)
            print(f"¿Lo ha hecho ya? [y/n]")
            r = input()
            if r == 'y':
                aux = True
            else:
                aux = False

        print(f"Por favor, introduzca el nombre EXACTO (nombre + extensión) de tu archivo de video:")
        name = input()  # Este será el nombre del archivo que vamos a utilizar en todos los ejercicios.
        # Comprovaremos que realmente existe:
        if look_file(name):
            return name
        else:
            return defaultName
    if resp == 'n':
        return defaultName

def look_file(name):
    mediaFolder = (
            "/Users/edwjunior/Documents/UNIVERSIDAD/4o CURSO/1r TRIMESTRE/SISTEMES DE CODIFICACIÓ D'ÀUDIO I VIDEO"
            "/SEMINARS/SEMINAR 3/media/" + str(name) + "")
    print(f"Buscando...")
    time.sleep(2)
    if os.path.isfile(mediaFolder):
        b = True
        print(f"El archivo se ha encontrado! \U0001F973")
        time.sleep(1)
    else:
        b = False

        print(f"No se ha encontrado ningún archivo...  \U0001F630")
        print(f"Se utilizará el archivo por defecto.")
        time.sleep(1)
    return b

def previous_main():

    defaultName = 'Resistencia_BM19.mp4'
    print(f"Bienvenido al Seminario 3 de Sistemas de Codificación de Video.")
    fileName = test_material(defaultName)
    print(fileName)
    return fileName


name = previous_main()
s3_main(name)
sys.exit()



