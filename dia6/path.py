from pathlib import Path

base = Path.home()
guia = Path(base,'Antioquia',Path('Medellin','Valerias.tbx'))
guia2 = guia.with_name("ElTrapiche.txt")

print(guia.parent.parent)