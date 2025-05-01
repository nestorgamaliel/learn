import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el archivo CSV (asegúrate de reemplazar 'archivo.csv' con el nombre correcto)
ruta = r"g:\My Drive\Estudios\UMA\UMA2025\Ciencia de datos\Presentaciones\4. alumnos_examen_errores.csv"
print(ruta)
df = pd.read_csv(ruta)

# Mostrar las primeras filas del dataset para verificar su estructura
print(df.head())

# Contar los valores de la columna 'Aprobó' (Sí/No)
aprobados = df['Aprobó'].value_counts()

print(aprobados)
print(type(aprobados))


# Crear el gráfico de pastel
plt.figure(figsize=(6, 6))
plt.pie(aprobados, labels=aprobados.index, autopct='%1.1f%%', colors=['lightgreen', 'red'], startangle=90)
plt.title('Porcentaje de estudiantes que aprobaron')
plt.show()


# Contar los valores de la columna 'Sexo' (Masculino/Femenino)
generos = df['Sexo'].value_counts()

# Crear el gráfico de pastel
plt.figure(figsize=(6, 6))
plt.pie(generos, labels=generos.index, autopct='%1.1f%%', colors=['blue', 'pink'], startangle=90)
plt.title('Distribución de estudiantes por género')
plt.show()


# Filtrar los estudiantes aprobados
df_aprobados = df[df['Aprobó'] == 'Sí']

# Contar cuántos hombres y mujeres aprobaron
aprobados_por_genero = df_aprobados['Sexo'].value_counts()

# Contar el total de hombres y mujeres
total_por_genero = df['Sexo'].value_counts()

# Calcular el porcentaje de aprobación por género
porcentaje_aprobados = (aprobados_por_genero / total_por_genero) * 100

# Crear gráfico de barras para comparar eficiencia de aprobación
plt.figure(figsize=(6, 6))
sns.barplot(x=porcentaje_aprobados.index, y=porcentaje_aprobados.values, palette=['blue', 'pink'])

# Agregar etiquetas y título
plt.ylabel('Porcentaje de aprobación (%)')
plt.xlabel('Género')
plt.title('Porcentaje de aprobación por género')

# Mostrar valores en las barras
for i, v in enumerate(porcentaje_aprobados.values):
    plt.text(i, v + 1, f"{v:.1f}%", ha='center', fontsize=12)

# Mostrar el gráfico
plt.show()