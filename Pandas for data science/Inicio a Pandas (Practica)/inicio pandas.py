import pandas as pd

# Cargar datos desde un archivo CSV
df = pd.read_csv("Clases/Data/pokemon.csv")

# Ver las primeras y ultimas filas del DataFrame
print("Primeras filas del DataFrame:")
print(df.head())

print("Ultimas filas del DataFrame:")
print(df.tail())

# Obtener informacion general sobre el DataFrame
print("Informacion del DataFrame:")
print(df.info())

#Generar estadisticas descriptivas
print("Estadisticas descriptivas del DataFrame:")
print(df.describe())

# Inspeccionar los tipos de datos de las columnas
print("Tipos de datos de las Columnas")
print(df.dtypes)

# Contar valores unicos en una columna especifica
print("Conteo de valores unicos en la columna 'Type 1':")
print(df['Type 1'].value_counts())

#Obtener valores unicos en una columna especifica
print("Valores unicos en la columna 'Type 1':")
print(df['Type 1'].unique())

# Obtener el numero de valores unicos en una columna especifica
print("Numero de valores unicos en la columna 'Type 1':")
print(df['Type 1'].nunique())

#Renombrar una columna
df.rename(columns={'Type 1': 'Tipos'}, inplace=True)
print("DataFrame con columna renombrada:")
print(df.head())

#Cambiar el indice del DataFrame
df.set_index('#', inplace=True)
print("DataFrame con nuevo indice:")
print(df.head())
