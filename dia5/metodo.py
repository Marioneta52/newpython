#lstrip borra datos de una cadena
print(",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#".lstrip(',:%_#'))

#insert inserta elemento a lista
frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(3, "naranja")
print(frutas)

#isdisjoint(). verifica elementos en comun
marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG",}


conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)
print(conjuntos_aislados)
