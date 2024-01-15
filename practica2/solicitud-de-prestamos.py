
#Maria fue a solicitar un préstamo de 100,000 pesos al banco BHD, y lo quiere a 12 meses.
#El banco le presta a una tasa de interés anual del 16.33%. Haga un script en python que 
#le permita a Maria conocer el monto de la cuota a pagar. (Usar la formula de amortización 
#francés, y comparar el resultado con la calculadora de prestamos de ProUsuario que 
#debe dar igual).

montoSolicitado = 100000
interes = 0.1633
meses = 12

cuotas = ((montoSolicitado * interes) + montoSolicitado) / 12

print(cuotas)