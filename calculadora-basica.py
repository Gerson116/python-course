
#Desarrollar una calculadora que trabaje con datos en memoria que ejecute las siguiente operaciones:
#(sumar, restar, multiplicar, dividir).

def SumarDosNumeros(num1, num2):
    resultado = int(num1) + int(num2)
    print(f"Resultado: {num1} + {num2} = {resultado}")

def RestarDosNumeros(num1, num2):
    resultado = int(num1) - int(num2)
    print(f"Resultado: {num1} - {num2} = {resultado}")

def MultiplicarDosNumeros(num1, num2):
    resultado = int(num1) * int(num2)
    print(f"Resultado: {num1} x {num2} = {resultado}")

def DividirDosNumeros(num1, num2):
    resultado = int(num1) / int(num2)
    print(f"Resultado: {num1} / {num2} = {resultado}")

SumarDosNumeros(25, 30)
RestarDosNumeros(25, 30)
MultiplicarDosNumeros(25, 30)
DividirDosNumeros(25, 30)