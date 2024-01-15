
#Ana contrató una maquina expendedora de cigarros en su mercado. Favor hacer un script en 
#python que solicite al usuario el numero de su edad y que muestre un mensaje en consola
#diciendo si es mayor de edad o menor de edad.

edadDelUsuario = int(input('Ingrese su edadd: '))

if edadDelUsuario >= 18:
    print(f"Su edad es: {edadDelUsuario} y es mayor de edad")
else:
    print(f"Su edad es: {edadDelUsuario} y es menor de edad")