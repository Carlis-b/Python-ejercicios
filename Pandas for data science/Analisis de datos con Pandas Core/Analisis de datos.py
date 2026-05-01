import pandas as pd
df = pd.read_csv("/Users/carlis/mi_proyecto/Pandas for data science/Analisis de datos con Pandas Core/data/vgsales.csv")

# Ver las primeras filas del DataFrame
print("Primeras filas del DataFrame:")
print(df.head(10))

#Exploracion inicial de datos
print("Ultimas filas del DataFrame:")
print(df.tail(5))

print("Informacion del DataFrame:")
print(df.info())

print("Estadisticas descriptivas del DataFrame:")
print(df.describe())

#Inspeccion de los datos
print("Tipos de datos de las Columnas")
print(df.dtypes)

print("Conteo de valores unicos en la columna 'Genre':")
print(df['Genre'].value_counts())

print("Valores unicos en la columna 'Platform':")
print(df['Platform'].unique())

#Filtrado de datos
filtro_NA_Sales = df[df['NA_Sales'] > 1]
print(filtro_NA_Sales)

filtro_JP_Sales = df[df['JP_Sales'] < 0.1]
print(filtro_JP_Sales)

filtro_action = df.query('Genre == "Action" and Global_Sales > 2')
print(filtro_action)

#Slicing de datos
df_columnas = df[["Name", "Global_Sales"]]
print(df_columnas)

df_loc = df.loc[5:10, ["Name", "Genre"]]
print(df_loc)

df_iloc = df.iloc[0:5, 0:3]
print(df_iloc)
