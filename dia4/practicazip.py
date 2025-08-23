#Mostrar en pantalla el mensaje la capital de xx es XX utilizando zip
capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

capital_mundo =list(zip(capitales,paises))
for vrCapital,vrPais in capital_mundo:
  print(f"La capital de {vrPais} es {vrCapital}")

#Crea un objeto zip formado a partir de listas, de un conjunto de marcas y productos que tú prefieras, dentro de la variable mi_zip.
marcas = ['apple', 'Cocacola', 'Mastercard', 'Ford', 'IBM']
productos = ['Iphone', 'Gaseosas', 'Creditos', 'Aumoviles', 'Software']
mi_zip = list(zip(marcas, productos))
print(mi_zip)

espaniol = ["uno", "dos", "tres", "cuatro", "cinco"]
portugues = ["um", "dois", "três", "quatro", "cinco"]
ingles = ["one", "two", "three", "four", "five"]

numeros = list(zip(espaniol, portugues, ingles))
print(numeros)
