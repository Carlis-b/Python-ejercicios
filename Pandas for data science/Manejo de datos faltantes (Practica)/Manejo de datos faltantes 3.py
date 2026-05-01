import pandas as pd
import numpy as np

#Crear un DataFrame de ejemplo
data = {'nombre': ['Ana', 'Luis', 'Carlos', 'Marta', 'Pedro'], 'edad': [28, 35, np.nan, 42, 25], 'cuidad': ['Madrid', np.nan, 'Barcelona', 'Valencia', np.nan]}
df = pd.DataFrame(data)

#Mostrar el DataFrame de ejemplo
print("DataFrame original:")
print(df)

#Eliminar filas con datos faltantes
df_sin_filas_nulas = df.dropna()
print("DataFrame sin filas con datos faltantes:")
print(df_sin_filas_nulas)

#Eliminar columnas con datos faltantes
df_sin_columnas_nulas = df.dropna(axis=1)
print("DataFrame sin columnas con datos faltantes:")
print(df_sin_columnas_nulas)