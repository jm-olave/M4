
# agregacion
class Estudiante:
    def __init__(self,id,nombre):
        self.__id = id
        self.nombre = nombre

    def get_id(self):
        return self.__id
    

    def numero_registro(self, id_departamento):
        self.__id = self.__id + id_departamento
        return self.__id
    
    



class Departamento:
    def __init__(self,id, estudiante):
        self.__id = id
        self.estudiante = estudiante

    def registro_estudiante(self):
        return self.estudiante.numero_registro(self.__id)


estudiante_1 = Estudiante(10, "Jorge")
departamento_1 = Departamento(12, estudiante_1)
print(departamento_1.registro_estudiante())




# Composicion
class DepartamentoC:
    def __init__(self,id, id_estudiante, nombre_estudiante):
        self.__id = id
        self.estudiante = Estudiante( id_estudiante, nombre_estudiante)

    def registro_estudiante(self):
        return self.estudiante.numero_registro(self.__id)
    
departamento_2 =DepartamentoC(8, 4, "Vivian")
print(departamento_2.estudiante.nombre)

