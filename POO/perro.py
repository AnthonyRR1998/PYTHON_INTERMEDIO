class Perro:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    
    def ladrar(self):
        print(f"{self.nombre} ladra fuerte")

    def __str__(self):
        return f"{self.nombre} de {self.edad}"

perro_1 = Perro("Rayder",3)
print(perro_1)

print(perro_1.nombre)
print(perro_1.edad)
print(perro_1.__str__())
perro_1.ladrar()