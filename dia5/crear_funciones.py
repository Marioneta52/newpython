#se inicia la funcion con def el codigo debe de estar tabulado despues del def

#funcion saludar_persona
def saludar_persona(nombre):
    print("Hola " + nombre)

def saludar():
    print("Hola mundo")

def bienvenida(nombre_persona):
    print("Hola " + nombre_persona)
nombre_persona = "Emilio Tapia"

#Potencia
def cuadrado(un_numero):
    print(un_numero**2)


#llamado funciones
saludar_persona('Alambrito Delgado')
saludar()
bienvenida(nombre_persona)
cuadrado(50)