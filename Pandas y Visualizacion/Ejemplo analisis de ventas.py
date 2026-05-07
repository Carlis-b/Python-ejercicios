import pandas as pd

#Crear un DataFrame de ejemplo
data = {'Producto': ['Manzanas', 'Naranjas', 'Platanos', 'Manzanas', 'Naranjas', 'Platanos'], 'Ventas':[50, 30, 20, 60, 40, 30], 'Precio':[0.5, 0.75, 0.3, 0.55, 0.8, 0.35]}
df = pd.DataFrame(data)

#Calcular el ingreso total por venta
df['Ingreso'] = df.apply(lambda row: row['Ventas'] * row['Precio'], axis=1)

#Calificar los productos por rango de ventas
df['Clasificacion'] = df['Ventas'].apply(lambda x: 'Alta' if x >40 else 'Baja')

#Normalizar la columna ventas
max_ventas = df['Ventas'].max()
min_ventas = df['Ventas'].min()
df['Ventas_normalizado'] = df['Ventas'].apply(lambda x: (x - min_ventas)/(max_ventas - min_ventas))

#Mostrar el DataFrame resultante
print(df)