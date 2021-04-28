import random

print("Bienvenido")

print("Seleccione una opción")
print("1.- Dados")
print("2.- ATM")
print("3.- Salir")
opcInicio = input("")
opc = int(opcInicio)

## funciones

def func_ATM(usuario):
    
    print("Bienvenido "+usuario)
    print("Seleccione qué quiere hacer")
    print("1.- Cargar dinero.")
    print("2.- Retirar dinero.")
    print("3.- Mostrar Saldo.")
    print("4.- Salir de la app.")
    opcAtm = input("ingrese opción: ")
    opcNueva = int(opcAtm)
    if opcNueva == 1:
        cargaDinero()
    if opcNueva == 2:
        retiroDinero()

def cargaDinero():
    print("Ingrese dinero a cargar, no pueden ser valores más altos que $200.000: ")
    cargaDinero = int(input())
    if cargaDinero > 200000:
        print("Error, no puede cargar más de $200.000")
        print("Volviendo al menú principal...")
        func_ATM(usuario)
    else:
        saldoNuevo = saldo + cargaDinero
        print("Saldo nuevo: $"+(str)(saldoNuevo))
        print("Gracias, volviendo al menú principal...")
        func_ATM(usuario)

def retiroDinero():
    print("Cuanto dinero desea retirar? No puede ser mayor a su saldo: ")
    retiroDinero = int(input())
    if(retiroDinero > saldo):
        print("error, retiro no puede ser mayor a saldo")
        print("Volviendo al menú principal...")
        func_ATM(usuario)
    else:
        saldoNuevo = retiroDinero - saldo
        print("Su nuevo saldo es: "+saldoNuevo+". Volviendo al menú principal...")
        func_ATM(usuario)
    
def func_Dados():
    (dado) = ['1','2','3','4','5','6']
    print("Seleccione T para tirar el dado.")
    opcDado = input()
    if(opcDado == 'T' or opcDado == 't'):
        print("Número: " +random.choice(dado))
        print("Desea tirar de nuevo el dado? s/n ")
        opcNueva = input()
        if opcNueva == 's' or opcNueva =='S':
            func_Dados()
        else:
            print("Gracias por participar.")
    else:
        print("Error, Seleccione la tecla T")
        func_Dados()


## Main del programa

saldo = 0

if opc == 1:
    print("Bienvenido a los D A D O S")
    func_Dados()
if opc == 2:
    print("Bienvenido a A T M")
    usuario = input("Ingrese nombre de usuario: ")
    password = input("Ingrese contraseña: ")
    func_ATM(usuario)
if opc == 3:
    print("Gracias, vuelva pronto.")


