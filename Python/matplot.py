
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.plot(x, y, marker='o', linestyle='-', color='b')
plt.title("Gráfico de Líneas")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.grid()
plt.show()


etiquetas = ["A", "B", "C", "D"]
valores = [5, 7, 3, 8]

plt.bar(etiquetas, valores, color='green')
plt.title("Gráfico de Barras")
plt.xlabel("Categorías")
plt.ylabel("Valores")
plt.show()


