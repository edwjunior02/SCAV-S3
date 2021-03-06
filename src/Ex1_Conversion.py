import time
import os
import shutil
srcFolder = (
            "/Users/edwjunior/Documents/UNIVERSIDAD/4o CURSO/1r TRIMESTRE/SISTEMES DE CODIFICACIÓ D'ÀUDIO I VIDEO"
            "/SEMINARS/SEMINAR 3/src")
mediaFolder = (
            "/Users/edwjunior/Documents/UNIVERSIDAD/4o CURSO/1r TRIMESTRE/SISTEMES DE CODIFICACIÓ D'ÀUDIO I VIDEO"
            "/SEMINARS/SEMINAR 3/media")

class E1:
    # Función que cambia los códecs de video según la variable (string) conversion_type y el nombre del archivo raíz..
    fileName = ''
    croppedName = ''
    def convert(self, conversion_type):
        point_pos = self.croppedName.index('.')  # cogemos la posición del punto.
        prev_name = self.croppedName[:point_pos]  # Seleccionamos toda la string menos la extensión.
        if conversion_type == 'VP8':
            os.system("ffmpeg -i "+str(prev_name)+".mp4 -c:v libvpx -q:a 0 "+str(prev_name)+"_vp8.webm")
            print(f"Mostrando resultado...")
            time.sleep(2)
            os.system("ffmpeg -i "+str(prev_name)+"_vp8.webm")
            time.sleep(5)
        elif conversion_type == 'VP9':
            os.system("ffmpeg -i "+str(prev_name)+".mp4 -c:v libvpx-vp9 -q:a 0 "+str(prev_name)+"_vp9.webm")
            print(f"Mostrando resultado...")
            time.sleep(2)
            os.system("ffmpeg -i "+str(prev_name)+"_vp9.webm")
            time.sleep(5)
        elif conversion_type == 'H.265':
            os.system("ffmpeg -i "+str(prev_name)+".mp4 -c:v libx265 -x265-params crf=19 "+str(prev_name)+"_h265.mov")
            print(f"Mostrando resultado...")
            time.sleep(2)
            os.system("ffmpeg -i "+str(prev_name)+"_h265.mov")
            time.sleep(5)
        elif conversion_type == 'AV1':
            os.system("ffmpeg -i "+str(prev_name)+".mp4 -c:v libaom-av1 -strict -2 -c:a libopus "+str(prev_name)+"_av1.avi")
            print(f"Mostrando resultado...")
            time.sleep(2)
            os.system("ffmpeg -i "+str(prev_name)+"_av1.avi")
            time.sleep(5)
        else:
            pass
        pass
        print(f"¡Convertido correctamente!")

    # Función que nos importa los archivos necesarios para trabajar desde la carpeta media/.
    def importFiles(self, srcFolder, mediaFolder, name):
        if not os.path.isdir(mediaFolder):
            print('la primera carpeta no existe')
        elif not os.path.isdir(srcFolder):
            print('la segunda carpeta no existe')

        contenidos = os.listdir(mediaFolder)
        self.fileName = name
        filename = self.fileName
        for elemento in contenidos:
            try:
                if elemento == filename:
                    print(f"Copiando {elemento} --> {srcFolder} ... ", end="")
                    src = os.path.join(mediaFolder, elemento)  # origen
                    dst = os.path.join(srcFolder, elemento)  # destino
                    shutil.copy(src, dst)
                    time.sleep(2)
                    print("Correcto")
                else:
                    continue
            except:
                print("Falló")
                print("Error, no se pudo copiar el archivo. Verifique los permisos de escritura")

        print(f"Se han importado los archivos correctamente.")
        time.sleep(2)

    # Función que nos mueve los archivos a su carpeta origen (media/) una vez hemos trabajado con ellos.
    def moveFiles(self, srcFolder, mediaFolder):
        contenidos = os.listdir(srcFolder)
        name = self.fileName[:self.fileName.index('.')]
        for elemento in contenidos:
            try:
                if elemento.startswith(name):
                    print(f"Moviendo {elemento} --> {mediaFolder} ... ", end="")
                    src = os.path.join(srcFolder, elemento)  # origen
                    dst = os.path.join(mediaFolder, elemento)  # destino
                    shutil.move(src, dst)  # Ahora utilizamos move en vez de copy, ya que lo queremos mover de aquí.
                    time.sleep(2)
                    print("Correcto")
                else:
                    continue
            except:
                print("Falló")
                print("Error, no se pudo copiar el archivo. Verifique los permisos de escritura")

        time.sleep(2)
        print(f"Se han movido los archivos correctamente.")

    # Función que nos prepara el archivo principal (vídeo) para optimizar rendimiento y reducir tiempos de compilación.
    def prepareMaterial(self):
        point_pos = self.fileName.index('.')  # cogemos la posición del primer punto.
        prev_name = self.fileName[:point_pos] # seleccionamos los caracteres previos a este punto.
        # Reducir duración a 20 segundos de video.
        os.system("ffmpeg -ss 00:01:40 -to 00:02:00 -i "+str(self.fileName)+" -vcodec copy -acodec copy "+str(prev_name)+"_cropped_20s.mp4")
        # Bajar resolución al mínimo.
        os.system("ffmpeg -i "+str(prev_name)+"_cropped_20s.mp4 -vf scale=720:480 "+str(prev_name)+"_cropped_480p.mp4")
        # Ya tenemos el video preparado para su conversión.
        self.croppedName = str(str(prev_name)+"_cropped_480p.mp4")
    # Función principal desde donde se llaman al resto de funciones.
    def main(self, fileName):
        self.fileName = fileName
        self.importFiles(srcFolder, mediaFolder)
        print(f"¡Bienvenido al ejercicio 1 del seminario 3 de Sistemas de Codificación de Audio y Video! \U0001F61C")
        print(f"Antes que nada, vamos a bajar mucho la resolución y duración de este video puesto que estos codecs tardan mucho en codificarse.")
        self.prepareMaterial()
        print(f"Ahora vamos a proceder a cambiar el codec de vídeo de nuestro video ya preparado! \U0001F61D")
        aux = True
        while aux == True:
            print(f"Selecciona el codec al que desea convertir el vídeo:")
            print(f"....................................")
            print(f". 1. VP8 en contenedor WebM:       .")
            print(f". 2. VP9 en contenedor WebM        .")
            print(f". 3. H.265 en contenedor MOV       .")
            print(f". 4. AV1 en contenedor MKV         .")
            print(f".                                  .")
            print(f". 5. Quiero pirarme de aquí:       .")
            print(f"....................................")
            res = input()
            if res == '5':
                option = input(f"Estas seguro que desea salir del programa? \U0001F62D [y/n]")
                if option == 'y':
                    aux = False
                    self.moveFiles(srcFolder, mediaFolder)
                    from main import s3_main
                    s3_main(self.fileName)
                else:
                    continue
            elif res == '1':
                type = 'VP8'
                print(f"Convirtiendo a VP8:")
                i = 0
                while i < 10:
                    print(f"\U0001F37A", end="")
                    i = i + 1
                    time.sleep(0.2)
                self.convert(type)
                continue

            elif res == '2':
                type = 'VP9'
                print(f"Convirtiendo a VP9:")
                i = 0
                while i < 10:
                    print(f"\U0001F37A", end="")
                    i = i + 1
                    time.sleep(0.2)
                self.convert(type)
                continue

            elif res == '3':
                type = 'H.265'
                print(f"Convirtiendo a H.265:")
                i = 0
                while i < 10:
                    print(f"\U0001F37A", end="")
                    i = i + 1
                    time.sleep(0.2)
                self.convert(type)
                continue

            elif res == '4':
                type = 'AV1'
                print(f"Convirtiendo a AV1:")
                i = 0
                while i < 10:
                    print(f"\U0001F37A", end="")
                    i = i + 1
                    time.sleep(0.2)
                self.convert(type)
                continue

