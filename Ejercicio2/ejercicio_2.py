print ("-----------------------------------------")
print ("----------multiplo de 7 o 9--------------------")
print ("-----------------------------------------")

multiplos_7, multiplos_9=0,0

rta = "rango = |"
for i in range (1000,5001):
    if i%7 == 0:
        multiplos_7 +=1
    if i%9 == 0:
        multiplos_9 +=1

print(f"cantidad de multiplos de 7 {multiplos_7}")
print(f"cantidad de multiplo de 9 {multiplos_9}")