import random

num_caras = 6

num_lanzamientos = int(input("Ingrese el número de lanzamientos: "))

frecuencia = [0] * num_caras
for i in range(num_lanzamientos):
    lanzamiento = random.randint(1,num_caras)
    frecuencia[lanzamiento-1] += 1
    
for cara, conteo in enumerate(frecuencia):
    print(f'Cara {cara+1}: {conteo} {"*" * conteo}')
# Imprimir los resultados con una barra de asteriscos
print(f"Lanzamientos{lanzamiento}")
print(f"Lanzamientos{i}")
print(f"Lanzamientos{frecuencia}")