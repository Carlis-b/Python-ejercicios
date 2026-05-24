import pandas as pd
df = pd.read_csv("Clases/Data/pokemon.csv")

print("\nCantidad de pokemones legendarios:")
print(df['Legendary'].nunique(True))

pokemon_total_mayor_500 = df[df['Total']> 500]
print(pokemon_total_mayor_500)


