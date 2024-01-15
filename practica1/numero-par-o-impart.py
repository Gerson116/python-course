
#Su sobrino necesita saber si el numero 5 es par o impar. Haga un script en python que guarde 
#el numero en una variable, lo evalúe y muestre un mensaje en la consola diciendo "True" si el
#numero es par o "False" si es impar. (Solo debe usar expresiones, no puede usar la condicional IF
numeroCinco = 5
cincoEsPar = numeroCinco % 2
if cincoEsPar == 0:
    print(f"{numeroCinco} Es par")
if cincoEsPar > 0:
    print(f"{ numeroCinco} No es par")


#Su sobrino necesita saber si un numero es par o impar. Haga un script en python que 
#reciba un numero por teclado y muestre un mensaje en la consola diciendo si el 
#numero es par o impar.

numero = input('Ingresa un numero par -> ')
result = int(numero) % 2

if result == 0:
    print(f"El numero: {numero} es par: {True}")
else:
    print(f"El numero: {numero} es impar: {False}")