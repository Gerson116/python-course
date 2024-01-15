
#Tu sobrino necesita calcular el area de un circulo para su clase de matemáticas.
#Haz un script que le permita hacer este cálculo solicitando el ingreso del 
#diámetro del radio del circulo a medir (la formula es la constante PI multiplicada
#por el diámetro del radio al cuadrado).

circulo = float(input('ingresa el valor del circulo.'))
pi = 3.1416
radio = circulo / (2 * pi)
area = pi * (radio * radio)

print(f"El area del circulo es igual a: {area}")