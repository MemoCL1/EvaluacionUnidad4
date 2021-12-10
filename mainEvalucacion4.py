"""AGREGAMOS LAS CLASES CERADAS """
import ClassesEvaluacion4 as Entidad
empleado1=Entidad.persona("Pepe","Macias",26,1.85,80,1500,"3 DE AGOSTO","UNIFORME")

clienta1=Entidad.persona("Alexa","Peña",68,1.50,50,300,"8 DE MAYO DE AGOSTO","VESTIDO")

Gerente=Entidad.persona("Ramon","valdez",45,1.85,80,2000,"3 DE AGOSTO","TRAJE")

print("ERA UN DIA NORMAL EN LA TIENDA CUANDO DE REPENTE")
clienta1.entrar()
empleado1.saludar()
clienta1.Quejarse()
empleado1.preguntar()

