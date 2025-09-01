import os
from pathlib import Path
#ruta = 'C:\\Workspace\\newpython\\dia6\\Recetario\\Recetas'

def mostrar_menu_directorio():
    ruta = Path('C:\\Workspace\\newpython\\dia6\\Recetario\\Recetas')

    carpetas = [c for c in os.listdir(ruta) if os.path.isdir(os.path.join(ruta, c))]

    for i, carpeta in enumerate(carpetas, start=1):
        print(f"{i}. 📁 {carpeta}")
        ruta_carpeta = os.path.join(ruta, carpeta)
        print(ruta_carpeta)
        archivos = [a for a in os.listdir(ruta_carpeta) if os.path.isfile(os.path.join(ruta_carpeta, a))]

        if archivos:
            for j, archivo in enumerate(archivos, start=1):
                print(f"   {i}.{j} 📄 {archivo}")
        else:
            print("   (No hay archivos en esta carpeta)")


# Solicitar ruta al usuario
#ruta_usuario = input("Ingrese la ruta del directorio: ").strip()
#mostrar_menu_directorio(ruta_usuario)

mostrar_menu_directorio()


