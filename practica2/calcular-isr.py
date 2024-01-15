

#Luis fue contratado como programador Jr. en python con un salario de 55,000 pesos. 
#Haga un script en python con el que pueda calcular el impuesto sobre la renta, que le
#descontarán mensualmente. (ver tabla ISR DGII)

salarioAnual = 660000
primerGrupoISR = 416220.01

excedente = salarioAnual - primerGrupoISR
isr = (excedente * 15) / 100

print(F"El ISR mensual es igual a: {isr/12}")