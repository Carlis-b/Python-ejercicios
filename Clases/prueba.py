import pandas as pd
df = pd.read_csv("Clases/Data/titanic.csv")

print("Primeras filas del DataFrame:")
print(df.head())

print(df.info())

print(df.describe())

print(df.dtypes)

print(df.head(10))

print(df.tail(10))