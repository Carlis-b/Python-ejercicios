import pandas as pd
import numpy as np

#Crear un DataFrame de ejemplo
data = {'fecha': pd.date_range(start= '1/1/2022', periods=10), 'ventas': [100, 200, np.nan, 400, 500, np.nan, 700, 800, 900, np.nan]}
df = pd.DataFrame(data)

#Interpolacion de valores faltantes
df['ventas'] = df['ventas'].interpolate()
print(df)

#Relleno hacia adelante de valores faltantes
df['ventas'] = df['ventas'].ffill()
print(df)

#Relleno hacia atras de valores faltantes
df['ventas'] = df['ventas'].bfill()
print(df)