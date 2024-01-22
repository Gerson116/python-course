# Realizar un programa que reciba por teclado el sueldo de un empleado y le
# aplique los cálculos de ISR (ver tabla DGII), ARS, y AFP (investigar porcentajes)

def main():
    salarioMensual = float(input(""""Ingrese su salario mensual para que conozca los
descuentos que son aplicados:
ARS
AFP
ISR\n
En el caso de este ultimo no es aplicable para todos los salarios. -> """))
    salarioAnual = salarioMensual * 12
    print(salarioAnual)
    isr = 0
    ars = 0
    afp = 0
    RANGO_SALARIAL_APLICABLE_ISR = 416220.01
    totalDescuentos = 0
    salarioNeto = 0

    if salarioAnual >= RANGO_SALARIAL_APLICABLE_ISR:
        isr = calcularISR(salarioAnual)
        afp = calcularAFP(salarioAnual)
        ars = calcularARS(salarioAnual)
        totalDescuentos = isr + afp + ars
        print(f"ISR: {isr}\nAFP: {afp}\nARS: {ars}")
    else:
        afp = calcularAFP(salarioAnual)
        ars = calcularARS(salarioAnual)
        totalDescuentos = isr + afp + ars
        print(f"AFP: {afp}\nARS: {ars}")
    
    salarioNeto = salarioMensual - totalDescuentos
    print(f"Su salario Bruto es de: {salarioMensual} y aplicando los descuentos su salario Neto es de: {salarioNeto}")


def calcularISR(salario):
    totalISR = 0
    PRIMER_GRUPO_ISR_DESDE = 416220.01
    PRIMER_GRUPO_ISR_HASTA = 624329.00
    SEGUNDO_GRUPO_IRS_DESDE = 624329.01
    SEGUNDO_GRUPO_ISR_HASTA = 867123.00
    TERCER_GRUPO_ISR_DESDE = 867123.01

    isrCalculado = 0
    montoAdicional = 0
    excedenteISR = 0

    if salario >= PRIMER_GRUPO_ISR_DESDE and salario <= PRIMER_GRUPO_ISR_HASTA:
        #...
        totalISR = 0.15
        excedenteISR = salario - PRIMER_GRUPO_ISR_DESDE
        isrCaculado = (excedenteISR * totalISR) / 12

    if salario >= SEGUNDO_GRUPO_IRS_DESDE and salario <= SEGUNDO_GRUPO_ISR_HASTA:
        montoAdicional = 31216.00
        totalISR = 0.20
        excedenteISR = salario - SEGUNDO_GRUPO_IRS_DESDE
        isrCaculado = ((excedenteISR * totalISR) + montoAdicional) / 12
        
    if salario >= TERCER_GRUPO_ISR_DESDE:
        montoAdicional = 79776.00
        totalISR = 0.25
        excedenteISR = salario - TERCER_GRUPO_ISR_DESDE
        isrCaculado = ((excedenteISR * totalISR) + montoAdicional) / 12
    
    return isrCaculado

def calcularAFP(salario):
    TASA_AFP_EMPLEADO = 0.0287
    afpCalculado = (salario * TASA_AFP_EMPLEADO)/12
    return afpCalculado

def calcularARS(salario):
    TASA_ARS_EMPLEADO = 0.015
    arsCalculado = (salario * TASA_ARS_EMPLEADO)/12
    return arsCalculado

main()