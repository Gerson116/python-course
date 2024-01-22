
# 5- Cree una aplicación de cajero automático para el banco ABC. El cajero tendrá un
# límite de billetes descrito a continuación: 9 de 1000, 19 de 500, 99 de 100
# El cajero debe solicitar Banco y monto a retirar. Si el banco es ABC el limite de
# retiro son 10,000 y 2000 pesos por transacción en caso contrario.
# El cajero debe informar si el monto solicitado no puede ser dispensado o si
# excede el límite de transacción. Y debe hacer la distribución de los billetes de
# acuerdo al monto. Por ejemplo, si el usuario solicita 3,900 y hay disponibilidad en
# todos los billetes, el cajero debe dispensar 3 billetes de mil, 1 de quinientos y 4 de
# cien.

def main():
    dineroATM = 28400
    cantidadMaximaDeBilletesDeMil = 9
    cantidadMaximaDeBilletesDeQuiniento = 19
    cantidadMaximaDeBilletesDeCien = 99

    montoPorTransaccion = 2000
    maximoRetirable = 10000

    billetesDeMilEntregados = 0
    billetesDeQuinientosEntregados = 0
    billetesDeCienEntregados = 0

    retiro = float(input("Ingresa la cantidad que desea retirar -> "))

    if retiro <= maximoRetirable:
        divicionBilletesDeMil = retiro / 1000

        if divicionBilletesDeMil > 1:
            billetesDeMilEntregados = divicionBilletesDeMil - (divicionBilletesDeMil % 1)
            
            if round((divicionBilletesDeMil % 1), 0) >= 0:
                redondearModQ = (divicionBilletesDeMil % 1) * 10
                divisionDeBilletesDeQuiniento = redondearModQ / 5
                billetesDeQuinientosEntregados = divisionDeBilletesDeQuiniento - (divisionDeBilletesDeQuiniento % 1)
                
                if (redondearModQ - 5) >= 0:
                    billetesDeCienEntregados = redondearModQ - 5

        if retiro >= 500 and retiro < 1000:
            divisionDeBilletesDeQuiniento = retiro / 500
            billetesDeQuinientosEntregados = divisionDeBilletesDeQuiniento - (divisionDeBilletesDeQuiniento % 1)
            if (retiro - 500) > 0:
                divisionDeBilletesDeCien = (retiro - 500) / 100
                billetesDeCienEntregados = divisionDeBilletesDeCien


        if retiro >= 100 and retiro <= 499:
            divisionDeBilletesDeCien = retiro / 100
            billetesDeCienEntregados = divisionDeBilletesDeCien - (divisionDeBilletesDeCien % 1)
        
        cantidadEnBilletesDeMil = billetesDeMilEntregados * 1000
        cantidadEnBilletesDeQuiniento = billetesDeQuinientosEntregados * 500
        cantidadEnBilletesDeCien = billetesDeCienEntregados * 100
        resultadoTotal = cantidadEnBilletesDeMil + cantidadEnBilletesDeQuiniento + cantidadEnBilletesDeCien
        print(f"El dinero dispensado fue de {resultadoTotal}\nBilletes de Mil: {billetesDeMilEntregados}\nBilletes de Quiniento: {billetesDeQuinientosEntregados}\nBilletes de Cien: {billetesDeCienEntregados}")
    else:
        print("La cantidad que desea retirar supera lo que se puede dispensar.")

main()