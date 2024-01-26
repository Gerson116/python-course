
def main():
    #...
    cantidadDeNumeros = int(input("Cuantos numeros va a ingresar? -> "))
    anterior = 0
    count = 0

    while count < cantidadDeNumeros:
        #...
        nuevo = int(input("Ingresa un número -> "))
        if nuevo > anterior and anterior == 0 :
            anterior = nuevo
            count += 1
            continue
        elif nuevo > anterior:
            #
            print(f"El numero {nuevo} es mayor al que ingreso anteriormente {anterior}")
            anterior = nuevo
        elif nuevo < anterior:
            # print(f"El numero {nuevo} es menor al que ingreso anteriormente {anterior}")
            anterior = nuevo
        anterior = nuevo
        count += 1

main()