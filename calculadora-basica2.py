import os
#Desarrollar una calculadora que solicite al usuario ingresar dos numeros y en caso de no insertar un numero,
#debe indicar al usuario que tiene que agregarlo. Luego debe solicitar la operacion que debe realizar y 
#acto seguido debe solicitar que ingrese otro numero.

def main():
    print("""Bienvenidos a la calculadora.
          Esta calculadora solo realiza operaciones matematicas como:
          suma, resta, multiplicacion y division""")

    num1 = 0
    resultadoDeLaOperacion = 0
    while num1 == 0:
        try:
            num1 = float(input("Favor ingresar el primer valor: -> "))
        except ValueError:
            limpiarPantalla()
            print("Ocurrio un error, favor insertar el primer valor de tipo numerico")

    resultadoDeLaOperacion = menuSolicitudes(num1)
    while resultadoDeLaOperacion >= 0:
        resultadoDeLaOperacion = menuSolicitudes(resultadoDeLaOperacion)

def menuSolicitudes(num1):
    num2 = 0
    comando = ""
    while comando == "":
        try:
            tempComando = input("""Favor ingresar escribe una de las operaciones que deseas realizar: 
                                \"sumar\", \"restar\", \"multiplicar\", \"dividir\". """)
            comando = tempComando.lower().strip() if operacionQueDeseaRealizar(tempComando) else ""

        except ValueError:
            limpiarPantalla()
            print("Ocurrio un error, favor insertar una de las operaciones aceptadas por el sistema.")

    while num2 == 0:
        try:
            num2 = float(input("Favor ingresar el segundo valor: -> "))

        except:
            limpiarPantalla()
            print("Ocurrio un error, favor insertar el primer valor de tipo numerico")

    resultadoDeLaOperacion = ejecutarOperaciones(comando, num1, num2)
    print(f"Resultado de la operacion: {resultadoDeLaOperacion}")
    return resultadoDeLaOperacion


def operacionQueDeseaRealizar(comando):
    if comando == "sumar":
        return True
    elif comando == "restar":
        return True
    elif comando == "multiplicar":
        return True
    elif comando == "dividir":
        return True
    else:
        return False

def ejecutarOperaciones(comando, num1, num2):
    result = 0
    if comando == "sumar":
        result = num1 + num2

    if comando == "restar":
        result = num1 - num2
        
    if comando == "multiplicar":
        result = num1 * num2

    if comando == "dividir":
        result = num1 / num2
    
    return result

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