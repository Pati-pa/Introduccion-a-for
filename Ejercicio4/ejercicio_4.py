n=int(input("Ingrese la cantidad de número a leer: "))

factorial=1

for i in range(1, n+1):
    factorial= factorial*i
    print(f"el factorial del {n} dado es {factorial}")