#numero y minimo
lista = [1,2,3,4,5,6,7,8,9,100,1000]
print(f"El menor es {min(lista)} y el mayor es {max(lista)}")

#En String
nombres = ["Jhon","Parlos","Emilio","Tapia","Zapata"]
print(min(nombres),max(nombres))
#Nota, ordena alfabeticamente y tiene en cuenta las iniciales en mayuscula


#En Diccionarios busca la clave más pequeña, pero si buscamos el valor encuentra el dato más pequeño
dic = {"c1":45, "c2":11}
print(min(dic.values()))
