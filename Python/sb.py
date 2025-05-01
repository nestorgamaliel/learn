import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el conjunto de datos "tips"
df = sns.load_dataset('tips')

# Crear un gráfico de dispersión entre "total_bill" y "tip"
sns.scatterplot(x='total_bill', y='tip', data=df)

# Mostrar el gráfico
plt.show()


fig, axes = plt.subplots(1, 2, figsize=(12, 6))
sns.histplot(df['total_bill'], kde=True, ax=axes[0])
sns.boxplot(x='day', y='total_bill', data=df, ax=axes[1])
plt.tight_layout()
plt.show()

