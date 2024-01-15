
#Carlos va a ir al cajero a hacer un retiro al cajero. en su cuenta tiene un 
#balance de 1584.23. El cajero solo entrega billetes de 100. haga un script en 
#python que solicite el monto del retiro. si el monto del retiro es mayor que el 
#monto disponible, debe decirle por consola que no tiene fondos suficientes para 
#la transacción. Si ingresa una cantidad que no se puede entregar con billetes de 
#100 (ej. 125, 1015, 150, 90) debe decirle que el monto solicitado no puede ser dispensado. 
#Si tiene fondos y marca un monto válido, debe imprimir en consola la cantidad de billetes 
#de 100 que se dispensaran.

cuentaBancaria = 1584.23
dineroRetirado = float(input('Ingresa la cantidad que desea retirar -> '))
cantidadDeBilletes = 0

if dineroRetirado > cuentaBancaria:
    print(f"Actualmente posee {cuentaBancaria} y la cantidad {dineroRetirado} que quiere retirar es superior")
else:
    if dineroRetirado < 100:
        print(f"Este cajero solo entrega billetes de 100")
    else:
        cantidadDeBilletes = int(dineroRetirado / 100)
        print(f"Acaba de retirar {cantidadDeBilletes}")