import numpy as np
import pandas as pd

#Crear un DataFrame de ejemplo
data = {'A':[1, 2, 3, 4], 'B':[10,20,30,40]}
df = pd.DataFrame(data)

#Calcular desviacion absoluta media
mean_A = df['A'].mean()
df['MAD_A'] = df['A'].apply(lambda x: np.abs(x - mean_A))
print(df)
