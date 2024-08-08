#polimosfirmo
class Animal:

    def hablar(self):
        pass
class Perro(Animal):
    def hablar(self):
        print("Guau!")
class Gato(Animal):
    def hablar(self):
        print ("miau!")

class Vaca(Animal):
    def hablar(self):
        print("Muu!")

animales = [Perro(),Gato(),Vaca()]

for animal in animales:
    animales.hablar()