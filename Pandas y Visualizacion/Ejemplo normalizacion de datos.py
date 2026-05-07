import pandas as pd

#Crear un DataFrame de ejemplo
data = {'Producto':['A', 'B', 'C', 'D'], 'Ventas':[200, 300, 400, 500]}
df =pd.DataFrame(data)

#Normalizar la columna Ventas
max_value = df['Ventas'].max()
min_value = df['Ventas'].min()
df['Ventas_normalizado'] = df['Ventas'].apply(lambda x: (x - min_value)/(max_value - min_value))
print (df)
