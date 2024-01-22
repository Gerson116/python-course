
# 3- Hacer un programa que genere las tablas de multiplicar de los números
# múltiplos de 5 que hay entre 1 y 1000

def main():
    count = 0
    multiplosDeCinco = []
    while count < 1000:
        count += 1
        mod = count % 5
        if mod == 0:
            multiplosDeCinco.append(count)

    for item in multiplosDeCinco:
        tablaDeMultiplicacion(item)

def tablaDeMultiplicacion(tabla):
    count = 0
    while count < 13:
        count += 1
        print(f"{count} x {tabla} = {count * tabla}")
    print("-------------------------------------------------------------------------------------------------------")

main()