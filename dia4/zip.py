#Zip permite nunir dos listas en tupples convinados
#lista Nombres
nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
edades = [20,43,64,12,35,15,18,34,83]
ciudades = ["Medellin","Lima","Cartagena","Madrid","Mexico","Mara","Valencia", "Cali","New york"]
combinados = list(zip(nombres, edades,ciudades))

#print(list(combinados))
for nombre,edad,ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")