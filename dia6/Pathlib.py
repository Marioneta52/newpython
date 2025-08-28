from pathlib import Path

carpeta = Path('/home/elitebook/Documentos/PUNTACANA2.txt')
print(carpeta.parents[3])

if not carpeta.exists():
    print("ESte archivo no Existe")
else:
    print('Archivo existe')
