import json
class Usuario:
    def __init__(self, id, nombre, edad, email):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.email = email


lista_usuarios = []
# lectura
with open("usuario.json", "r") as documento:
    lectura = json.load(documento)
    for usuario in lectura:
        user_object = Usuario(usuario["id"], usuario["nombre"], usuario["edad"], usuario["email"])
        lista_usuarios.append(user_object)
        print(usuario["nombre"], usuario["edad"])

# escritura
datos = [
    {"nombre": "Manzana", "color": "rojo"},
    {"nombre": "Mango", "color": "verde"},
    {"nombre": "Naranja", "color": "naranja"}
]
# escritura
with open("frutas.json", "w") as documento:
    json.dump(datos, documento)

print(lista_usuarios[0].nombre)