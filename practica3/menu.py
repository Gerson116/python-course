import os

def main():
    print("""Menu de opciones: 
1- Convertir grados a Celsius a Fahrenheit
2- Convertir dólar a pesos
3- Convertir metros a pies
4- Salir\n""")

    menu = int(input("Ingresa la opción -> "))
    salir = 4

    while menu != salir:
        try:
            menuSolicitudes(menu)
            menu = int(input("Ingresa la opción -> "))
        except ValueError:
            limpiarPantalla()
            print("Ocurrio un error, favor insertar el primer valor de tipo numerico")
    limpiarPantalla()

def menuSolicitudes(menu):
    #...
    convertirDeCelsiusAFahrenheit = 1
    convertirDolarPesos = 2
    convertirMetrosAPies = 3
    salir = 4

    if convertirDeCelsiusAFahrenheit == menu:
        # Conversión de celsius a fahrenheit
        celsiusAFahrenheit()

    if convertirDolarPesos == menu:
        # Conversión de celsius a fahrenheit
        conversionDolarAPesos()

    if convertirMetrosAPies == menu:
        # Conversión de celsius a fahrenheit
        conversionMetrosAPies()

def celsiusAFahrenheit():
    #...
    celsius = float(input("Ingrese la temperatura en celsius -> "))
    fahrenheit = (celsius * 1.8) + 32
    print(f"La temperatura en Fahrenheit: {fahrenheit}")

def conversionDolarAPesos():
    cantidadDeDolares = float(input('Ingresa la cantidad de dolares ->'))
    cantidadEnPesos = cantidadDeDolares * 57.40
    print(f"Al convertir su cantidad en dolares: {cantidadDeDolares}, posee una cantidad en pesos: {cantidadEnPesos}")

def conversionMetrosAPies():
    #...
    metros = float(input('Ingresa la cantidad de metros -> '))
    pies = (metros * 3.28) / 1.0
    print(f"La cantidad de metros: {metros} en pies es igual a: {pies}")


def limpiarPantalla():
    operationSystem = os.name
    posix = "posix" # macOS and Linux
    nt = "nt" # Windows

    if operationSystem == posix:
        os.system('clear')
    elif operationSystem == nt:
        os.system('cls')
    else:
        print("No reconocemos el sistema operativo con el que esta operando.")

main()