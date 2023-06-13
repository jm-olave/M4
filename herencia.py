class Perro:
    # metodo constructor
    def __init__(self, nombre, edad):
        
        self.nombre = nombre
        self.edad = edad

    #metodos 
    def correr(self, velocidad):
        return f'Estoy corriendo!! a {velocidad}'
    

class Labrador(Perro):
    def __init__(self, nombre, edad, jugueton, color):
        super().__init__(nombre, edad)
        self.jugueton = jugueton
        self.color = color  
    def nadar(self):
        return "estoy nadando"
    def correr(self, velocidad):
        print("estoy sacando la lengua")
        velocidad += 10
        return super().correr(velocidad)
    
    
class Dalmata(Perro):
    pass


labrador_1 = Labrador("Copito", 6, True, "rojo")
dalmata_1 = Dalmata("ray", 4)
print(labrador_1.nombre)
print(labrador_1.jugueton)
print(labrador_1.correr(12))
print(dalmata_1.correr(12))