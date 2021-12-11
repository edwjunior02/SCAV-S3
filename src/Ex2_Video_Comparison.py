import sys
import time
import os
import shutil
from Ex1_Conversion import E1


class E2:

    srcFolder = ("/Users/edwjunior/Documents/UNIVERSIDAD/4o CURSO/1r TRIMESTRE/SISTEMES DE CODIFICACIÓ D'ÀUDIO I VIDEO"
                 "/SEMINARS/SEMINAR 3/src")
    mediaFolder = ("/Users/edwjunior/Documents/UNIVERSIDAD/4o CURSO/1r TRIMESTRE/SISTEMES DE CODIFICACIÓ D'ÀUDIO I VIDEO"
                   "/SEMINARS/SEMINAR 3/media")

    name = ''

    def select_media(self, ext, name):
        pass
        # Esta función nos va a detectar si se ha encontrado algún archivo con la extensión solicitada.
        content = os.listdir(self.mediaFolder)
        print(ext)
        point_pos = name.index('.')  # cogemos la posición del punto.
        prev_name = name[:point_pos]  # Seleccionamos toda la string menos la extensión.
        for element in content:
            try:
                if element.startswith('Resistencia_BM19') and element.find(str(ext)):
                    print(element.title())
                    print(f"Copiando {element} --> {self.srcFolder} ... ", end="")
                    src = os.path.join(self.mediaFolder, element)  # origen
                    dst = os.path.join(self.srcFolder, element)  # destino
                    shutil.copy(src, dst)
                    time.sleep(2)
                    print("Correcto")
                elif element.startswith('Resistencia'):       # ERROR: ESTA HACIENDO ESTE ELSE PARA CADA ARCHIVO QUE NO SEA EL DE VP8 !!!!!!!
                        print(f"Falló")
                        print(f"No existe ningún elemento con este formato.")
                        time.sleep(1)
                        aux = True
                        while aux == True:
                            print(f"¿Desea generar un archivo con este nuevo fomato? [y/n]")
                            resp = input()
                            if resp == 'y':
                                aux = False
                                E1.importFiles(self.srcFolder, self.mediaFolder)
                                E1.prepareMaterial()
                                print(f"Convirtiendo a " + str(ext) + ":")
                                i = 0
                                while i < 10:
                                    print(f"\U0001F37A", end="")
                                    i = i + 1
                                    time.sleep(0.2)
                                E1.convert(ext)
                            elif resp == 'n':
                                aux = False
                                print(f"Volviendo al principio...")
                                time.sleep(2)
                                self.main()
                            else:
                                print(f"La respuesta no es correcta. Vuelva a probar:")
                else:
                    continue

            except:
                print("Falló")
                print("Error, no se pudo copiar el archivo. Verifique los permisos de escritura")

    def main(self, name):
        # Llamamos al menu interactivo que nos desglosa el código.
        self.name = name
        self.menu()

    def menu(self):

        codec1 = None
        codec2 = None
        extension = None

        name = ''

        print(f"¡Bienvenido al ejercicio 2 del seminario 3 de Sistemas de Codificación de Audio y Video! \U0001F61C")
        print(f"En este ejercicio procederemos a comparar entre dos codecs de videos. Dos codecs que TU PODRÁS SELECCIONAR! \U0001F61D")
        print(f"Por favor, selecciona el primer codec que quieres comparar:")
        print(f"......................................................")
        print(f". 1. VP8 en contenedor WebM:                         .")
        print(f". 2. VP9 en contenedor WebM                          .")
        print(f". 3. H.265 en contenedor MOV                         .")
        print(f". 4. AV1 en contenedor MKV                           .")
        print(f".                                                    .")
        print(f". 5. Me he equivocado y no quiero comparar nada.:    .")
        print(f"......................................................")
        resp1 = input()
        if resp1 == '5':
            option = input(f"Estas seguro que desea salir del programa? \U0001F62D [y/n]")
            if option == 'y':
                sys.exit()
            else:
                self.menu()
        elif resp1 == '1':
            codec1 = '_vp8'
            self.name = conca
            extension = '.webm'
            self.select_media(codec1, extension)
        elif resp1 == '2':
            codec1 = '_vp9'
            extension = '.webm'
            self.select_media(codec1)
        elif resp1 == '3':
            codec1 = '_h265'
            extension = '.mov'
            self.select_media(codec1)
        elif resp1 == '4':
            codec1 = '-av1'
            extension = '.avi'
            self.select_media(codec1)
        # self.objectClass1.moveFiles(self.srcFolder, self.mediaFolder)
        # Ya que si no estaremos buscando en la carpeta media/ que no esta actualizada con los archivos que se han generado.
        print(f"Okey....")
        time.sleep(2)
        print(f"Por favor, selecciona el segundo codec que quieres comparar:")
        print(f"......................................................")
        print(f". 1. VP8 en contenedor WebM:                         .")
        print(f". 2. VP9 en contenedor WebM                          .")
        print(f". 3. H.265 en contenedor MOV                         .")
        print(f". 4. AV1 en contenedor MKV                           .")
        print(f".                                                    .")
        print(f". 5. Me he equivocado y no quiero comparar nada.:    .")
        print(f"......................................................")
        resp2 = input()
        if resp2 == '5':
            option = input(f"Estas seguro que desea salir del programa? \U0001F62D [y/n]")
            if option == 'y':
                import main
                main.s3_main()
            else:
                self.menu()
        elif resp2 == '1':
            codec2 = 'vp8'
            self.select_media(codec2)
        elif resp2 == '2':
            codec2 = 'vp9'
            self.select_media(codec2)
        elif resp2 == '3':
            codec2 = 'h265'
            self.select_media(codec2)
        elif resp2 == '4':
            codec2 = 'av1'
            self.select_media(codec2)
