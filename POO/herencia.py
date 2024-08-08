'''
crear una clase llamada deporte que tenga como atributos : nombre
crear 2 metodos:
uno que imprima el nombre del deporte
otro que imprima "Soy un deporte"

'''
class Deporte:

    def __init__(self,nombre):
        self.nombre = nombre

    def __str__(self):
        return f"El nombre del deporte es:{self.nombre}"
    
    def queDeporte(self):
        print(self.nombre + ": soy un deporte")

deporte_1 = Deporte("Nadar")
print(deporte_1)

deporte_1.queDeporte()

