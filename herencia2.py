
class Figura:
    def __init__(self, color):
        self.color = color

    def area(self):
        pass

    def mostrar_info(self):
        print(f'Color: {self.color}')


class Rectangulo(Figura):
    def __init__(self,alto, ancho, color ):
        super().__init__(color)
        self.alto = alto
        self.ancho = ancho
    def area(self):
        return self.alto * self.ancho
    def mostrar_info(self, tipo):
        super().mostrar_info()
        print(f' Tipo: {tipo}')
        print(f'Altura: {self.alto}')
        print(f'Ancho: {self.ancho}')

class Circulo(Figura):
    def __init__(self, radio, color):
        super().__init__(color)
        self.radio = radio
    
    def area(self):
        return 3.14 * (self.radio ** 2)
    def mostrar_info(self):
        super().mostrar_info()
        print(f'Tipo: Circulo', '\n',f'Radio: {self.radio}')

class Trapezio(Rectangulo):
    def mostrar_info(self, tipo):
        super().mostrar_info(tipo)
        print("esto es una trapezio")
        


rectangulo_1 = Rectangulo(12,13, "azul")
circulo_1 = Circulo(3, "Naranja")
trapezio_1 = Trapezio(10,10, "gris")

print(rectangulo_1.color)
rectangulo_1.mostrar_info("Rectangulo")
print(rectangulo_1.area())
figura_1 = Figura("rojo")
figura_1.mostrar_info()
circulo_1.mostrar_info()
trapezio_1.mostrar_info("Trapezio")
