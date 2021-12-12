import os.path
import time
import sys
from Ex1_Conversion import E1
from Ex2_Video_Comparison import E2
from Ex3_Live_Streaming import E3
from Ex4_IP_Broadcast import E4

def s3_main(fileName):
    print(f"Bienvenido al Seminario 3 de Sistemas de Codificación de Video.")
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
            s3_main()
    else:
        aux = 0
        while aux == 0:
            if ex == '1':
                self1 = E1()
                E1.main(self1, fileName)
            elif ex == '2':
                self2 = E2()
                E2.main(self2, fileName)
            elif ex == '3':
                self3 = E3()
                E3.main(self3, fileName)
            elif ex == '4':
                self4 = E4()
                E4.main(self4, fileName)
            else:
                time.sleep(1)
                print(
                    "\nNúmero de ejercicio incorrecto \U00002620. Introduce uno de las 5 opciones disponibles:')\n")
                return

fileName = 'Resistencia_BM19.mp4'       #Aquí se deberá cambiar el nombre del archivo si fuera necesario.
s3_main(fileName)
sys.exit()



