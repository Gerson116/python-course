
# Realizar un programa que solicite al usuario un número indeterminado de
# números (mientras se tecleen números que no sean cero). Al salir el programa
# debe dar en pantalla el total de números dados y la suma de ellos.

print("""Bienvenido a la sumadora, mientras ingreses un numero
diferente de cero el sistema ira sumando las cantidades.\n""")

numeroIndeterminado = float(input("Ingresa un numero diferente de cero -> "))
resultadoSuma = 0

while numeroIndeterminado != 0:
    numeroIndeterminado = float(input("Ingresa un numero diferente de cero -> "))
    resultadoSuma += numeroIndeterminado

print(resultadoSuma)