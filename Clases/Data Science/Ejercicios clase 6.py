temperaturas = [23.1, 19.8, 25.4, 17.2, 30.0, 22.5, 18.9, 27.3, 21.1, 24.6]

suma = 0
for temp in temperaturas:
    suma += temp
print(f"Suma: {suma}")

prom = suma / len(temperaturas)
print(f"Promedio: {prom: .2f}")

temperaturas.sort()
min = temperaturas[0]
max = temperaturas[-1]

print(f"Valor minimo: {min}")
print(f"Valor maximo: {max}")

contador = 0
for temp in temperaturas:
    if temp > prom:
        contador = contador + 1
print("Valores sobre promedio:", contador)
    
