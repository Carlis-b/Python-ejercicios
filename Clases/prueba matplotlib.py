import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("Clases/Data/pokemon.csv")

# Ver las primeras filas del DataFrame
print("Primeras filas del DataFrame:")
print(df.head(10))

#El tipo con mayor defensa promedio
promedio_defensa = df.groupby('Type 1')['Defense'].mean()
print(promedio_defensa)

import matplotlib.pyplot as plt

# La forma recomendada: fig, ax = plt.subplots()
fig, ax = plt.subplots(figsize=(8, 4))

# Datos simples
generaciones = [1, 2, 3, 4, 5, 6]
total_prom = df.groupby("Generation")["Total"].mean().values

ax.plot(generaciones, total_prom, color="#6C3CE1", linewidth=2.5, marker="o", markersize=8, markerfacecolor="#00C9A7")

ax.set_title("Stats Totales Promedio por Generación", fontsize=14, fontweight="bold", pad=14)
ax.set_xlabel("Generación", fontsize=12)
ax.set_ylabel("Total Promedio", fontsize=12)
ax.set_xticks(generaciones)
ax.grid(alpha=0.3, linestyle="--")

plt.tight_layout()
plt.show()
