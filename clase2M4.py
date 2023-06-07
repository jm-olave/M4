class CuentaDeBanco:

    # atributo de clase
    nombre_del_banco = "AwakeBank"

    # metodo constructor
    def __init__(self,numero,tipo,balance=0):
        # atributos de instancias
        # private
        self.__numero = numero
        self.tipo = tipo
        # public
        self.balance = balance
    # metodos get
    def getNumero(self):
        return self.__numero
    
    # metodos set
    def setNumero(self, numero):
        self._numero = numero
    def cargo(self, cantidad):
        self.balance += cantidad
    def abono(self, cantidad):
        self.balance += cantidad

    @staticmethod
    def get_nombre_banco():
        pass
    

class Transaccion:
    
    def __init__(self, cantidad, cuenta):
        self.cantidad = cantidad
        if isinstance(cuenta, CuentaDeBanco):
            self.cuenta = cuenta
        else:
            print("Error en la creacion de la Transaccion cuenta no es objeto apropiado")

    def ejecutar(self):
        if self.cantidad > 0:
            self.cuenta.abono(self.cantidad)
            print("tipo de cuenta:", self.cuenta.tipo)
        else:
            self.cuenta.cargo(self.cantidad)
            print("tipo de cuenta:", self.cuenta.tipo)


class Banco:
    def __init__(self):
        self.cuentasdebanco = []

    def crear_cuenta_de_banco(self, cuenta):
        self.cuentasdebanco.append(cuenta)

    def solicitar_prestamo(self, cuenta):
        if cuenta.balance > 500:
            print("prestamo aceptado para la cuenta", cuenta.getNumero())
        else:
            print("prestamo rechazado, balance menor a 500")




# objetos 
cuentadeVictor = CuentaDeBanco("1234574", "corriente", 1000)
print(cuentadeVictor.nombre_del_banco)
cuentadeCaterin = CuentaDeBanco("47367217", "ahorros", 500)
# print(cuentadeCaterin.numero)
cuentadeRodrigo = CuentaDeBanco(None,None)
print(cuentadeRodrigo.balance)
print(cuentadeRodrigo.getNumero())
CuentaDeBanco.get_nombre_banco()

# transacciones
print("balance de Victor :",  cuentadeVictor.balance)
transacciondeCargo = Transaccion(500, cuentadeRodrigo)
transacciondePago = Transaccion(300, cuentadeVictor)
transacciondePago.ejecutar()
print("balance de Victor actualizado :", cuentadeVictor.balance)

bancoAwakelab = Banco()
bancoAwakelab.crear_cuenta_de_banco(cuentadeCaterin)
bancoAwakelab.crear_cuenta_de_banco(cuentadeRodrigo)
bancoAwakelab.solicitar_prestamo(cuentadeCaterin)
for i in bancoAwakelab.cuentasdebanco:  
    print(i.getNumero())