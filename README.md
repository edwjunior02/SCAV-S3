# SCAV-S3
#### Eduard Pui - 194161 - eduard.puig02@estudiant.upf.edu

## EJECRICIO 1: CONVERSIÓN
En este primer ejercicio, se nos pedía realizar varias conversiones de un video de muestra (nosotros seguiremos utilizando el vídeo ```Resistencia_BM19.mp4```) 
a ciertos codecs de vídeo como son ```VP8, VP9, H.265 Y AV1```.
Se tratan de codecs de actual importancia debido a que son los que se estan aplicando en casi todas las plataformas multimedia como Netflix, AmazonPrime, YouTube,etc.
Pero cada uno tiene sus ventajas e inconvenientes (algo que queda fuera del contexto de este seminario).
Primero de todo tenemos el script ```Ex1_Conversion.py``` que incluye la clase ```E1``` con todas las funciones declaradas e implementadas
que nos ayudarán a realizar la tarea requerida.
Estos son los pasos que sigue el código:
```
1. Importar/cargar el archivo de vídeo en a raíz del proyecto.
2. Reducir duración y resolución para no sobrecargar el proyecto con esperas largas y tediosas.
3. Selección codec.
4. Conversión
```
Los primeros pasos son los "preparativos" para poder realilzar lo que realmente importa de este ejercicio: CONVERTIR EL VÍDEO CON OTRO CODEC.
Tenemos que destacarque el programa comprime la resolución del vídeo a 480p (720:480) y reducimos su duración a 20s.

ATENCIÓN: Para que todo funcione correctamente, deberemos de escribir el path de la carpeta multimedia (la que contiene el material audiovisual) y la carpeta raíz (donde se guardan los scripts):
```ruby
srcFolder = ("PATH/src")
mediaFolder = ("PATH/media")
```
Una vez cargado todo y reducido resolución y duración, aparecerá un menú en el que podremos escoger el codec que vamos a transcodificar:

<<CARGAR IMÁGEN MENÚ EJERCICIO 1>>

Una vez hemos seleccionado la opción deseada, se ejecutara el bloque de código ```FFMPEG``` que permite convertir formatos de vídeos. 
En este bloque de código tenemos un ejemplo para convertir un input ```.mp4``` a un contenedor ```WebM``` con formato de vídeo ```VP8```:
```ruby
os.system("ffmpeg -i Resistencia_BM19_cropped_120p.mp4 -c:v libvpx -q:a 0 Resistencia_BM19_cropped_120p_vp8.webm")
```

Por último, se ha diseñado el programa para que automáticamente aparezca una comprovación del archivo mediante el comando:
```ruby
os.system("ffmpeg -i <Nombre_Archivo_flags.extension")
```
Y aparecerá el resultado siguiente:

<<CARGAR IMÁGEN RESULTADO EJERCICIO 1>>