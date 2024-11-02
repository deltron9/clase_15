from datetime import datetime
'''
Disponemos de los siguientes datos obtenidos de una lista de
reproducción del cantante Emanero:

Tema: “Karina | J mena | Angela - Sinvergüenza”

Vistas: “45.8 millones”

Duración: “228”

Link: “https://www.youtube.com/watch?v=AhZvCgk1Ay4”

Fecha Lanzamiento: “2023-12-05”

Nos piden desarrollar las siguientes funciones, para un posterior
análisis de la lista de reproducción.

1. obtener_colaboradores(str) -> list: recibe como parámetro el
título del tema y retorna una lista con todos los colaboradores.

2. obtener_nombre_tema(str) -> str: retorna el nombre del tema.

3. convertir_vistas_numerico(str)->int: convertirá la cantidad de
vistas a un número entero expresado en millones.

4. convertir_duracion_numerico(str)->int: convertirá la duración a
un número entero.

5. obtener_codigo(str)->str: retorna el código de la url recibida
como parámetro.

6. formatear_fecha(str): retorna la fecha recibida por parámetro
como un objeto de tipo fecha 😉
'''

titulo = 'Karina | J mena | Angela - Sinvergüenza'

vistas = '45.8 millones'

duracion = '228'

link = 'https://www.youtube.com/watch?v=AhZvCgk1Ay4'

fecha_lanzamiento = '2023-12-05'

def obtener_colaboradores(titulo):
    return titulo.split(' - ')[0].split(' | ')

def obtener_nombre_tema(titulo):
    return titulo.split(' - ')[1]

def convertir_vistas_numerico(vistas):
    return int(float(vistas.split()[0]) * 1000000)

def convertir_duracion_numerico(duracion):
    return int(duracion)

def obtener_codigo(url):
    codigo = url.split('=')[-1]
    return codigo

def formatear_fecha(fecha_lanzamiento):
    return datetime.strptime(fecha_lanzamiento, '%Y-%m-%d').date()


def menu_filtro():
    while True:
        opciones_menu = f'[1]Obtener colaboradores \n[2]Obtener nombre del tema \n[3]Convertir vistas a número \n[4]Convertir duración a número \n[5]Obtener código de YouTube \n[6]Formatear fecha \n[7]Salir del programa. \n\nSeleccione una opción:'
    
        opcion = input(opciones_menu)
        
        match opcion:
            case '1':
                colaboradores = obtener_colaboradores(titulo)
                print(f'colaboradores: {colaboradores}')
                
            case '2':
                nombre_tema = obtener_nombre_tema(titulo)
                print(f'Nombre del tema: {nombre_tema}')
                
            case '3':
                vistas_numerico = convertir_vistas_numerico(vistas)
                print(f'vistas expresado en numero: {vistas_numerico}')
                
            case '4':
                duracion_numerico = convertir_duracion_numerico(duracion)
                print(f'duración en número: {duracion_numerico}')
                
            case '5':
                codigo = obtener_codigo(link)
                print(f'código de YouTube: {codigo}')
            case '6':
                fecha_formateada = formatear_fecha(fecha_lanzamiento)
                print(f'Fecha de lanzamiento: {fecha_formateada}')
            case '7':
                print('saliendo del programa...')
                break
                
            case _:
                print('Apretaste cualquier cosa rey')

menu_filtro()



