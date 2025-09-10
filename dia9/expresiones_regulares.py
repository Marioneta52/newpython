import re

texto = "Si necesitas ayuda llama al 658-598-9977 las 24 horas al servicio de ayuda online"

#buscar ayuda en el texto sin expresiones regulares
palabra = 'ayuda' in texto
print(palabra)

#informa en donde se encuentra la palabra
patron = 'online'
busqueda = re.search(patron, texto)
print(busqueda)


busqueda2 = re.findall(patron, texto)
for hallazgo in re.finditer(patron, texto):
    print(hallazgo.span())


#buscar el patron de telefono
#patron = r'\d\d\d-\d\d\d-\d\d\d\d'
#patron = r'\d{3}-\d{3}-\d{4}'
patron =re.compile(r'(\d{3})-(\d{3})-(\d{4})') # al compilarlo y ponerlo en parentesis puedo ejecutar .group y mostrar los grupos de numeros

resultado = re.search(patron, texto)
print(resultado.group(3))
