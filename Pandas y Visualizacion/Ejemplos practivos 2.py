import pandas as pd

#Crear un DataFrame de ejemplo
data = {'Cliente':['A', 'B', 'C', 'A', 'B', 'C', 'A'], 'Monto':[100, 200, 150, 300, 120, 180, 90], 'Compras':[1, 1, 1, 2, 2, 2, 3]}
df = pd.DataFrame(data)

#Agrupar por cliente
grouped = df.groupby('Cliente')

#Analizar la cantidad de compras y el monto total gastado por cada cliente
cantidad_compras = grouped['Compras'].count()
monto_total = grouped['Monto'].sum()

print("Candida de compras por cliente:")
print(cantidad_compras)

print("Monto total gastado por cliente:")
print(monto_total)