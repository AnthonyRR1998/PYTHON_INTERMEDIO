'''
Ejercicio
'''

class Persona:
    def __init__(self,nombre):
        self.nombre = nombre

class Estudiante(Persona):
    def __init__(self,nombre,carrera):
        super().__init__(nombre)
        self.carrera = carrera

    def __str__(self):
        return f"{self.nombre},carrera:{self.carrera}"
    
    def estudiar(self):
        print("Estudiando..."+ self.carrera)

estudiante_1 = Estudiante('Anthony R', 'Ingeniera')
print(estudiante_1)
estudiante_1.estudiar()
