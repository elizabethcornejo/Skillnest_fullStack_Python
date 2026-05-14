class CafeteriaCliente:
    total_clientes = 0

    def __init__(self, nombre):
        self.nombre = nombre
        self.puntos = 0
        self.saldo_pendiente = 0
        self.membresia = "Bronce"
        CafeteriaCliente.total_clientes += 1

    def realizar_compra(self, monto):
        self.saldo_pendiente += monto
        self.puntos += (monto // 1000) * 10
        print(f"{self.nombre} realizó una compra.")

    def pagar_saldo(self, monto):
        if monto <= self.saldo_pendiente:
            self.saldo_pendiente -= monto
            print(f"{self.nombre} pagó ${monto}.")
        else:
            print("No puede pagar más de lo que debe.")

    @classmethod
    def mostrar_total_clientes(cls):
        print(f"Total de clientes: {cls.total_clientes}")

    @staticmethod
    def validar_membresia(tipo):
        membresias = ["Bronce", "Plata", "Oro"]
        return tipo in membresias


cliente1 = CafeteriaCliente("krishna")
cliente2 = CafeteriaCliente("Camilo")
cliente3 = CafeteriaCliente("Teté")

cliente1.realizar_compra(5000)
cliente1.pagar_saldo(2000)

cliente2.realizar_compra(3000)
cliente2.pagar_saldo(5000)

CafeteriaCliente.mostrar_total_clientes()

print(CafeteriaCliente.validar_membresia("Oro"))
print(CafeteriaCliente.validar_membresia("Diamante"))
