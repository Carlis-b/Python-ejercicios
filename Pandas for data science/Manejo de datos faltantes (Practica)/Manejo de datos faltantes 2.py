import pandas as pd
import numpy as np

#Crear un DataFrame de ejemplo
data = {'estudiante': ['A', 'B', 'C', 'D', 'E'], 'calificacion': [85, 90, np.nan, 78, np.nan]}
df = pd.DataFrame(data)

#Rellenar valores nulos con la media de la columna
df['calificacion_media'] = df['calificacion'].fillna(df['calificacion'].mean())
print("Rellenar con la media:")
print(df)

#Rellenar valores nulos con la mediana de la columna
df['calificacion_mediana'] = df['calificacion'].fillna(df['calificacion'].median())
print("Rellenar con la mediana:")
print(df)

#Rellenar valores nulos con la moda de la columna
df['calificacion_moda'] = df['calificacion'].fillna(df['calificacion'].mode()[0])
print("Rellenar con la moda:")
print(df)