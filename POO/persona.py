class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"{self.nombre} {self.edad}"
    
    def saludar(self):
        print("Hola, mi nombre es: " + self.nombre+ " y tengo " + str(self.edad) + " años")
        
#Crear objetos
persona1 = Persona("Anthony Robayo",26)
print(persona1)

persona1.saludar()