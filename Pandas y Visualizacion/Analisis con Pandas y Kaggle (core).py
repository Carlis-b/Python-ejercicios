import pandas as pd

df = pd.read_csv("/Users/carlis/mi_proyecto/Pandas y Visualizacion/supermarket_sales 2.csv")

# Ver las primeras filas del DataFrame
print("Primeras filas del DataFrame:")
print(df.head(10))

#Exploracion inicial de datos
print("Ultimas filas del DataFrame:")
print(df.tail(5))

print("Informacion del DataFrame:")
print(df.info())

print("Estadisticas descriptivas del DataFrame:")
print(df.describe().round(2))

#Identificar valor nulos
print(df.isnull().sum())

print("Cantidad de nulos en la columna Date:")
print(df['Date'].isnull().sum())


#Corregir tipos de datos
print("Tipos originales:")
print(df.dtypes)

#en este caso se visualiza que la fecha esta en formato str segun lo revisdo en la red esto estaria bien al venir de un archivo csv pero para analizar datos por este medio ese formato no seria de ayuda por lo tanto se realiza este cambio
df['Date'] = pd.to_datetime(df['Date'], format="%m/%d/%Y")
print("Fecha convertida:")
print(df[['Date']].dtypes)

#Otro caso que nos interesa corregir sera la columna Quantity ya que se encuentra en float osea numero decimal y consideramos que para un mejor analisis es necesario que se cambie a numero entero
df['Quantity'] = df['Quantity'].astype(int)
print("Cantidad convertida:")
print(df[['Quantity']].dtypes)

#Confirmar si existen filas duplicadas
n_duplicados = df.duplicated().sum()
print(f"Filas duplicadas: {n_duplicados}")

col_duplicados = df.duplicated(subset=['Payment']).sum()
print(f"Columna payment duplicada: {col_duplicados}")
# para este caso se entiende que este bien que existan datos duplicados en la columna payment ya que esta columna indica el metodo de pago

#Transformacion de datos




#Analisis de datos
ventas_por_tienda = df.groupby('Branch')['Total'].sum()
print("Ventas por tienda:")
print(ventas_por_tienda)


