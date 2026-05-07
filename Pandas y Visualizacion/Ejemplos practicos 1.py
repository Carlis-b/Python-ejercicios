#Crear un DataFrame de ejemplo
import pandas as pd
data = {'Producto': ['Manzanas', 'Naranjas', 'Platanos', 'Manzanas', 'Naranjas', 'Platanos'], 'Mes':['Enero', 'Enero', 'Enero', 'Febrero', 'Febrero', 'Febrero'], 'Ventas':[100, 80, 50, 120, 90, 70]}
df = pd.DataFrame(data)

#Agrupar por Producto y Mes
grouped = df.groupby(['Producto', 'Mes'])

#Suma y promedio de ventar por producto y mes
ventas_por_producto_y_mes = grouped['Ventas'].agg(['sum', 'mean'])
print(ventas_por_producto_y_mes)