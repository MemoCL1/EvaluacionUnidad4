"Aqui van todoas las clases que se usaron y varios metodos"

class persona:

    def __init__(self,nombre,apellidos,edad,altura,peso,saldoCuenta,fechaNacimiento,vestimenta):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.altura = altura
        self.peso = peso
        self.credito = float(saldoCuenta)
        self.nacimiento = fechaNacimiento
        self.vestimenta = vestimenta

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

class Ropa:
    def __init__(self,color):
        self.color = color
        self.cierre = None
        self.botones = None
        self.bolsillos = None
        self.grande = None
        self.nuevo =None


