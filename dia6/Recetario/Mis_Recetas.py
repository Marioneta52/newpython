import os
from pathlib import Path
ruta = Path('C:\\Workspace\\newpython\\dia6\\Recetario\\Recetas')
opcion = 0

def directorioRecetas():
    directorio = [c for c in os.listdir(ruta) if os.path.isdir(os.path.join(ruta, c))]
    print('Se encontraros los siguientes Tipos De Menú:')
    for carpeta in enumerate(directorio, start=1):
        print({carpeta})
    opcion = int(input('Ingresa una  opción del Menú'))
    carpeta = directorio[ opcion  - 1]
    os.system('cls')
    return(carpeta, opcion)


def lista_recetas(carpeta):
    ruta_carpeta = Path(ruta).joinpath(carpeta)
    print('Se encontraros las siguientes Recetas:')
    archivo = [a for a in os.listdir(ruta_carpeta) if os.path.isfile(os.path.join(ruta_carpeta, a))]
    for receta in enumerate(archivo, start=1):
        print(receta)
    opcion = int(input('Ingresa una  opción del de la receta que desea '))
    receta = archivo[opcion - 1]
    os.system('cls')
    return carpeta,receta

def ver_receta(carpeta, receta):
    ruta_receta = Path(ruta).joinpath(carpeta)
    archivo_receta  = ruta_receta / receta[1]
    ruta_receta = open(archivo_receta)
    print(ruta_receta.read())


def menu_principal(opcion):
    os.system('cls')
    match opcion:
        case n if opcion  == 1:
            c,p = directorioRecetas()
            nomreceta = lista_recetas(c)
            ver_receta(c, nomreceta )
        case n if opcion == 2:
            c, p = directorioRecetas()
            nomreceta = lista_recetas(c)
        case n if opcion == 3:
            c, p = directorioRecetas()
            nomreceta = lista_recetas(c)



opmenu = int(input('Ingersa una opcion del menu \n'
                   '1: Leer receta \n'
                   '2: Modificar receta \n'
                   '3: Eliminar Receta \n'
                   '4: Salir \n'))
menu_principal(opmenu)

#carpeta, opcion = directorioRecetas()
#print(f'La opcion selecciónada es: {opcion} del menu de recetas {carpeta}')
#carpeta, nomreceta  = lista_recetas(carpeta)
#print(carpeta, nomreceta )
#ver_receta(carpeta, nomreceta )





