from Ex3_Live_Streaming import E3

class E4:

    def main(self, fileName):
        print(f"¡Bienvenido al ejercicio 4 del seminario 3 de Sistemas de Codificación de Audio y Video! \U0001F61C")
        print(f"En este ejercicio vamos a permitir escoger la IP local en la que se va a ''stremear'' el vídeo: \U0001F61D")
        print(f"Por favor, introduzca la ip a la que desea realizar el streaming (default: 192.168.1.37):")
        ip_address = input()
        print(f"Genial! Ahora introduzca el puerto de salida (default: 23000):")
        port = input()
        print(f"Cambiando IP a "+str(ip_address)+" y cambiando puerto a "+str(port)+"...")
        e3 = E3()
        E3.make_stream(e3, ip_address, port, fileName)
