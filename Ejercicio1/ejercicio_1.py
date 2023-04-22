# caso N°1 
print ("-----------------------------------------")
print ("----------Par o impar--------------------")
print ("-----------------------------------------")

numero_par= 0
numero_impar = 0
n=int(input("Ingrese la cantidad de número a leer: "))
for i in range(n):
    num= int(input("ingrese un número entero: "))
    if num % 2 == 0 :
        numero_par +=1
    else :
        numero_impar +=1
print(f"cantidad de numeros impar {numero_impar}")
print(f"cantidad de numeros impar {numero_par}")
