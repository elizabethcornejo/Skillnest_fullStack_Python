class Usuario:
def __init__(self, nombre, apellido, email):
    self.nombre = nombre
    self.apellido = apellido
    self.email = email
    self.limite_credito = 30000
    self.saldo_pagar = 0
def hacer_compra(self, monto):  #recibe como argumento el monto de la compra
    self.saldo_pagar += monto   #el saldo a pagar del usuario aumenta en la cantidad del valor recibido

#_______________________Ejercicio 1________________________________
def aumentarCredito(self, aumento):
    self.limite_credito += aumento
#_______________________Ejercicio 2 _______________________________
def cambiarCorreo(self, email)
    self.email = email




#instancias de la clase 
miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la")
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la")

miyagi.hacer_compra(2000)
print(f"Primera compra de ${miyagi.nombre}: ${miyagi.saldo_pagar}.")
miyagi.hacer_compra(300)
print(f"Segunda compra: ${miyagi.saldo_pagar}")
#cuanto credito le queda a miyagi 
print(f"Credito disponible: ${miyagi.limite_credito - miyagi.saldo_pagar}")

daniel.hacer_compra(45)
print(miyagi.saldo_pagar) #Imprime: 350
print(daniel.saldo_pagar) #Imprime: 45


#Tarea crear un nuevo 
'''
1.- crear un nuevo metodo que permita aumentar el limite de credito.
Imprimir el nuevo limite de credito.
'''

miyagi.aumentarCredito(2000)
print(f"Elnuevo limite de credito es: ${limite_credito}")

miyagi.cambiarCorreo("miyagisacamela@gmail.com")
print(f"El nuevo correo establecido es : {miyagi.email}")




'''
2.- crear un metodo que permita cambie el metodo de la instancia.
Mostrar el nuevo correo
'''
