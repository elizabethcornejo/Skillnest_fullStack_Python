class CafeteriaCliente:
    total_clientes = 0
    def __init__(self,nombre):
        self.nombre = nombre
        self.puntos = 0
        self.saldo_pendiente = 0
        self.membresia = "Bronce"
        CafeteriaCliente.total_clientes += 1 

    def realizar_compra(self, monto):
        self.saldo_pendiente += monto
        self.puntos += (monto // 1000) * 10
        print(f"{self.nombre} realizó una compra.")

usuario1 = CafeteriaCliente("Camilo")
usuario2 = CafeteriaCliente("arael")
usuario3 = CafeteriaCliente("Fernando")
