import datetime
import analizador.analizador_lexico as analizador

usuario_github = input("Ingrese su usuario de Github: ")
ruta_archivo = f'./algoritmos/algoritmo_{usuario_github}.rb'
with open(ruta_archivo, 'r') as archivo:
    algoritmo_ruby = archivo.read()
fecha_hora = datetime.datetime.now()
analizador.ejecutarAnalizador(algoritmo_ruby, usuario_github, fecha_hora)