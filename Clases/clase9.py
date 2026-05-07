import pandas as pd
df = pd.read_csv("Clases/Data/pokemon.csv")

# Ver las primeras filas del DataFrame
print("Primeras filas del DataFrame:")
print(df.head(10))

#El tipo con mayor defensa promedio
promedio_defensa = df.groupby('Type 1')['Defense'].mean()
print(promedio_defensa)

#Legendarios por generacion
cuenta_legendarios = df.groupby('Legendary')['Generation'].count()
print(cuenta_legendarios)


