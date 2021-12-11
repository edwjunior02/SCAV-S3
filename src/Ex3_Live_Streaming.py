import os
import time
from Ex1_Conversion import E1

class E3:
    srcFolder = ("/Users/edwjunior/Documents/UNIVERSIDAD/4o CURSO/1r TRIMESTRE/SISTEMES DE CODIFICACIÓ D'ÀUDIO I VIDEO"
                 "/SEMINARS/SEMINAR 3/src")
    mediaFolder = ("/Users/edwjunior/Documents/UNIVERSIDAD/4o CURSO/1r TRIMESTRE/SISTEMES DE CODIFICACIÓ D'ÀUDIO I VIDEO"
                   "/SEMINARS/SEMINAR 3/media")

    def main(self, fileName):
        ip_address = '192.164.1.37'
        port = 23000
        E1.importFiles(self.srcFolder, self.mediaFolder)
        print(f"¡Bienvenido al ejercicio 3 del seminario 3 de Sistemas de Codificación de Audio y Video! \U0001F61C")
        print(f"En este ejercicio procederemos a realizar un streaming de video a nivel local. \U0001F61D")
        print(f"Mientras se ejecuta el script, ve a una nueva ventana de terminal y ejecuta el comando: ffplay udp://"+str(ip_address)+":"+str(port)+"")
        print("Si no le deja a la primera, vuelva a probar (a veces los paquetes tardan un poco en llegar).")
        time.sleep(2)
        print(f"Esto le permitirá ver el streaming del video en tiempo real \U0001F61D")
        time.sleep(3)
        self.make_stream(ip_address, port)

    def make_stream(self, ip_address, port):
        os.system("ffmpeg -re -i Resistencia_BM19.mp4 -qscale 0 -f mpegts udp://" + str(ip_address) + ":" + str(port) + "")

