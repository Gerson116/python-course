

def main():
    #...
    montoSolicitado = float(input("Ingresa la cantidad que desea "))
    montoDelPrestamo = round(montoSolicitado, 2)
    interes = 0.1633
    meses = 12

    resultCuotasCapital = ((montoDelPrestamo * interes) + montoSolicitado) / 12
    cuotasCapital = round(resultCuotasCapital, 2)
    totalIntereses = round((((cuotasCapital * meses) - montoDelPrestamo) / 12), 2)

    count = 0
    while count < meses:
        print(f"Cuota: {count + 1} -- Capital: {cuotasCapital - totalIntereses} -- Interes: {totalIntereses}")
        count += 1

main()