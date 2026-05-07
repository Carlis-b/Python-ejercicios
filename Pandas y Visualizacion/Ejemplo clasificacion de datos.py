import pandas as pd

#Crear un DataFrame de ejemplo
data = {'Estudiante':['Ana', 'Luis', 'Carlos', 'Marta'], 'Calificacion':[85, 40, 72, 65]}
df = pd.DataFrame(data)

#Clasificar las calificaciones
df['Resultado'] = df['Calificacion'].apply(lambda x: 'Aprobado' if x >= 60 else 'Reprobado')
print(df)