import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el dataset
csv_path = "dataset_situacion_habitacional.csv"
df = pd.read_csv(csv_path)

# Mostrar información general
df.info()

# Mostrar primeras filas
print(df.head())

# Verificar valores nulos
print("Valores nulos por columna:")
print(df.isnull().sum())

# Estadísticas descriptivas
print(df.describe())

# Distribución del hacinamiento
plt.figure(figsize=(8, 5))
sns.histplot(df['Hacinamiento'], bins=20, kde=True)
plt.title('Distribución del Hacinamiento')
plt.xlabel('Personas por metro cuadrado')
plt.ylabel('Frecuencia')
plt.show()

# Relación entre ingreso y hacinamiento
plt.figure(figsize=(8, 5))
sns.boxplot(x=df['Ingreso_SMVM'], y=df['Hacinamiento'])
plt.title('Relación entre Ingreso y Hacinamiento')
plt.xlabel('Ingreso en Salarios Mínimos')
plt.ylabel('Hacinamiento')
plt.show()
