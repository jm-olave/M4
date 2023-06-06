class Perro:

    # metodo constructor
    def __init__(self, nombre, raza, edad, color):
        
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.color = color

    #metodos 
    def correr(self, velocidad):
        return f'Estoy corriendo!! a {velocidad}'

homero = Perro("homero","labrador",5,)
firulais = Perro("firulais","rotweiller",6,"negro")
print(homero.__dict__)
print(homero.correr(15))
print(firulais.raza)
print(firulais.nombre)
print(homero.nombre)

listaPerros = []
i = 2
while(i>0):
    nombre = input("ingrese nombre :")
    perro = Perro(nombre,"labrador",5, "golden")
    listaPerros.append(perro)
    i-=1
print(listaPerros[0].nombre)