"Aqui van todoas las clases que se usaron y varios metodos"

class persona:

    def __init__(self,nombre,apellidos,edad,altura,peso,saldoCuenta,fechaNacimiento):
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__edad = edad
        self.__altura = altura
        self.__peso = peso
        self.__credito = float(saldoCuenta)
        self.__nacimiento = fechaNacimiento

    def saludar(self):
        print("Hola buenos dias")

    def presentarse(self):
        print('Mi nombre es ', self.nombre)

    def presentarseFormalmente(self):
        print("Mi nombre completo es",self.__nombre,self.__apellidos)

class Empleado(persona):
    def __init__(self, nombre, altura, vestimenta, empresa, puesto):
        super().__init__(nombre, altura, vestimenta)
        self.empresa = empresa
        self.puesto = puesto

    def saludar(self):
        print(f'Hola me llamo {self.nombre} y soy empleado de {self.empresa}')

class Gerente(Empleado):
    def __init__(self, nombre, altura, vestimenta, empresa, puesto):
        super().__init__(nombre, altura, vestimenta, empresa, puesto)
        self.puesto = 'Gerente'

    def saludar(self):
        print(f'Soy el gerente de {self.empresa}, mi nombre es {self.nombre}')

    def entrevistar(self, persona):
        print(f'Estoy entrevistando a {persona}')