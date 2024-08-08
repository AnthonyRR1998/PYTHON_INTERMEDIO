class Cuadrilaterio:

    def __init__(self,lados):
        self.lados= lados
        self.suma_angulos = 360

    def perimetro(self):
        return sum(self.lados)
    
class Cuadrado(Cuadrilaterio):
    def __init__(self,lados):
        super().__init__(lados)#super()sirve para heredar metodos y atributos de la clase base

cuadrado_1 = Cuadrado([4,4,4,4])
perimetro_1 = cuadrado_1.perimetro()

print(perimetro_1)#16
print(cuadrado_1.suma_angulos)#360