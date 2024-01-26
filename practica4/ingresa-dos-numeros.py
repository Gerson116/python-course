

def main():
    print("Ingresa dos numeros enteros.")

    num1 = int(input("Ingresa el primer numero -> "))
    num2 = int(input("Ingresa el segundo numero -> "))
    count = num1
    tempValue = 0

    if(num1 < num2):
        #....
        while count < num2:
            count += 1
            if count == num1:
                continue
            elif count == num2:
                continue
            else:
                tempValue = count % 2
                parOImpar = lambda x: "par" if x == 0 else "impar"
                print(f"{count} - {parOImpar(tempValue)}")
    else:
        #.....
        print("El primero numero es mayor que el segundo numero.")

    # print('')


main()