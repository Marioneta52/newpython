#puedo mostrar solo alguno de los elementos de tupple asi:
precios_cafe = [('capuchino',3500),('Expresso',25500),('Moka',5300)]
for cafe,elemento in precios_cafe:
    print(cafe)

#Si quiero saber cuál se el cafe más caro con una funcion
def cafe_mas_caro(lista_precio):
    precio_mayor = 0
    cafe_mas_caro = ''
    for cafe, precio in lista_precio:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass

    return(cafe_mas_caro,precio_mayor)

cafe, precio = cafe_mas_caro(precios_cafe)
print(f'El cafe mas es: {cafe} vale {precio}')