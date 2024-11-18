import datetime
import analizadores.analizador_lexico as analizador

usuarios_github = ['dlaborde27','jordansalinasp10']
print('Seleccione su usuario de Github: ')
for i in range(len(usuarios_github)):
    print(f'{i+1}: {usuarios_github[i]}')

inputCorrecto = False
usuario_github = ''
while not inputCorrecto:
    seleccion = int(input("Digite una opción: "))
    if 0 < seleccion < 3:
        usuario_github = usuarios_github[seleccion-1]
        inputCorrecto = True
    else:
        print('Opción no válida, ingrese de nuevo')

ruta_archivo = f'./algoritmos/algoritmo_{usuario_github}.rb'

with open(ruta_archivo, 'r') as archivo:
    algoritmo_ruby = archivo.read()
fecha_hora = datetime.datetime.now()
analizador.ejecutarAnalizador(algoritmo_ruby, usuario_github, fecha_hora)
print(f'\n\nPrueba de {usuario_github} en {fecha_hora} realizada con éxito')
