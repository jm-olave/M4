
def dividir_numeros(a,b):
    try:
        resultado = a/b
        return resultado
    except Exception as error:
        print(f"Ocurrio un error: {error}")
    
    

def realizar_calculo(a,b,c):
    try:
        valor = dividir_numeros(a,b)
        resultado = valor * c
    except TypeError:
        print("Ocurrio un error: el dato de division o de multiplicacion es incorrecto")
    else:
        print(f'El resultado final {resultado}')
    finally:
        print("Linea de Finally")
        
    
   

realizar_calculo(10,0, 4)


# Crear una excepcion

class Usuario:
    pass
class AdalidExcepcion(Exception):
    def __init__(self, usuario):
        self.usuario = usuario
        super().__init__(f'tipo de Error: se genero un eror en el sistema Adalid por culpa del usuario {self.usuario}')


def procesamiento_de_datos(datos):
    if not datos:
        raise AdalidExcepcion(12)

def carga_de_archivo(path):
    if type(path) is not str:
        raise AdalidExcepcion("usuario.nombre")
    
try:
    procesamiento_de_datos([])
except Exception as variable:
    print(variable)
finally:
    variable = "manejado"
    print(variable)