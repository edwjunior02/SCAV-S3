import time
import sys
import Ex1_Conversion
import Ex2_Video_Comparison
import Ex3_Live_Streaming
import Ex4_IP_Broadcast


def s3_main():
    print(f"Bienvenido al Seminario 1 de Sistemas de Codificación de Video.")
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
            return
    else:
        aux = 0
        while aux == 0:
            if ex == '1':
                E1 = Ex1_Conversion.E1()
                E1.main()
            elif ex == '2':
                import Ex2
                Ex2.main()
            elif ex == '3':
                import Ex3
                Ex3.main()
            elif ex == '4':
                import Ex4
                Ex4.main()
            else:
                time.sleep(1)
                print(
                    "\nNúmero de ejercicio incorrecto \U00002620. Introduce uno de las 5 opciones disponibles:')\n")
                return
s3_main()
sys.exit()



