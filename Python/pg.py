import matplotlib.pyplot as plt
import pandas as pd
from sqlalchemy import create_engine

# Configurar la conexión con PostgreSQL
usuario = "lender"
contraseña = "lender1$"
host = "localhost"  # Cambia si usas un servidor remoto
puerto = "5432"
base_datos = "Lender"

# Crear la cadena de conexión
connection_string = f"postgresql://{usuario}:{contraseña}@{host}:{puerto}/{base_datos}"
engine = create_engine(connection_string)

    # Definir y ejecutar la consulta SQL
query = "SELECT * FROM alumnos"
df = pd.read_sql(query, engine)

# Mostrar las primeras filas del DataFrame
print(df.head())


print(df.info())  # Muestra el tipo de datos y valores nulos


print(df.describe())  # Muestra estadísticas como media, desviación estándar.


print(df.isnull().sum())  # Muestra cuántos valores nulos tiene cada columna

df_filtrado = df[df["Promedio"] > 9]
print(df_filtrado.head())


# Crear un histograma
plt.figure(figsize=(8,5))
plt.hist(df['Promedio'], bins=20, color='blue', edgecolor='black')
plt.title('Distribución de valores en Promedio')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.show()


plt.figure(figsize=(8,5))
plt.scatter(df['Carrera'], df['Promedio'], alpha=0.5, color='red')
plt.title('Relación entre columna_x y columna_y')
plt.xlabel('Columna X')
plt.ylabel('Columna Y')
plt.show()
