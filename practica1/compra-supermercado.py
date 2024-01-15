
#Juan hizo una compra en el supermercado, el valor de la compra sin impuestos
#fue de RD$16,760.74. Haga un script en python que calcule el ITBIS, un 
#descuento de 5% y el total a pagar.

montoCompra = 16760.74
itbis = (montoCompra * 18) / 100
descuento = (montoCompra * 5) / 100

totalPorPagar = (montoCompra - descuento) + itbis

print(f"Monto Compra: {montoCompra}\nITBIS: {itbis}\nDescuento: {descuento}\nMonto total a pagar: {totalPorPagar}")