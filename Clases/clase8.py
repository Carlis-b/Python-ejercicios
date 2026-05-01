import pandas as pd
df = pd.read_csv("Clases/Data/titanic.csv")
print(f"Shape: {df.shape}")
df.head()

# Encontrar valores nulos
nulos = df.isnull().sum()
print("Nulos por columna:")
print(nulos)

print()


#porcentaje nulos - mas util
pct_nulos = (df.isnull().sum() / len(df) * 100).round(1)
print("\n% de nulos por columna:")
print(pct_nulos[pct_nulos > 0])

#Ver las filas que tienen nulos en Age
df[df['Age'].isnull()] [['Name', 'Sex', 'Age', 'Pclass']].head(8)

