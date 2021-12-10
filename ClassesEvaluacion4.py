"Este programa muestra una simulacion de una oficina"

class persona:

    def __init__(self,nombre,apellidos,edad,altura,peso,saldoCuenta,fechaNacimiento):
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__edad = edad
        self.__altura = altura
        self.__peso = peso
        self.__credito = float(saldoCuenta)
        self.__nacimiento = fechaNacimiento