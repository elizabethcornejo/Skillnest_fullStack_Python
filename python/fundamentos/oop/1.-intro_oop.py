#creacion de la clase usuario-- Entidad 
class Usuario:
    def __init__(self): # Es el constructor de la clase 
        self.nombre = "Nariyoshi"
        self.apellido = "Miyagi"
        self.email = "miyagi@codingdojo.la"
        self.limite_credito = 30000
        self.saldo_pagar = 0


#instancias de una clase
miyagi = Usuario()  #"miyagi" es una variable # 
daniel = Usuario()
tete = Usuario()

#Accedemos a los atributos de la instancia
print(miyagi.nombre) #Imprime: Nariyoshi
print(daniel.nombre) #Imprime: Nariyoshi
print(miyagi.apellido)
print(miyagi.email)
print(miyagi.limite_credito)
print(miyagi.saldo_pagar)

#nuevos valores asignados a tributos de la instancia   
daniel.nombre = "Daniel"
daniel.apellido = "Larusso"
daniel.email = "miyagi@codingdojo.la"
daniel.limite_credito = 30000
daniel.saldo_pagar = 0

print(daniel.nombre) #Imprime: Daniel

#valores a nueva instancia 
tete.nombre = "teté"
tete.apellido = "cornejo"
tete.email = "tete@gmail.com"
tete.limite_credito = 1000
tete.saldo_pagar = 20000

# imprimir nombre de cada instancia 
print(tete.nombre)


