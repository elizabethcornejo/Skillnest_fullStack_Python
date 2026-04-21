# funciones en python 
def multiplicacion(num1, num2): #definimos la función multiplación con los parámetros num1 y num2
    resultado = num1 * num2     #instrucciones dentro de la función
    return resultado            #regresamos valor de resultado

a = int(input("Ingrese el primer numero"))
b = int(input("Ingrese el segundo numero"))
resultado_multiplicacion = multiplicacion(5, 5) #Llamado a la función con argumentos 5 y 5
print(resultado_multiplicacion) #Se guarda en la variable el resultado que la función regresó. Imprime: 25

#parametros y argumentos 
def buenos_dias(nombre):
    print("Buenos días "+nombre)
    # llamada a la funcion y asiganacion de valor a parametro
    buenos_dias("alegría")
    buenos_dias("al amor")
    buenos_dias("a la vida")
    buenos_dias("señor Sol")


    #devolucion de valores 

def buenos_dias(nombre):
    return "Buenos días "+nombre

#El valor de retorno de la función es "Buenos días Python", por lo que el valor de mi variable frase será ese

frase = buenos_dias("Python")
print(frase) #Imprime: Buenos días Python

# ejercicio de retorno da valor
# crear una funcion que reciba una frase mas un parametro,(una frase + una palabra)
# devolver el valor de la frase completa e imprimir.

def hola(nombre):
    print("HOLAAAAAA" +nombre)
    hola("tete")
    hola("dany")
    hola("camilo")
    hola("krishna")


    def hola(nomre):
        return "HOLLAAAAA" +nombre 

        Hola = hola("bello/a")
        print(Hola)


        