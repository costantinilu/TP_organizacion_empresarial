import pandas as pd
import matplotlib.pyplot as plt

# Leer datos
df = pd.read_csv("datos/ventas.csv")

# Calcular total
df["total"] = df["cantidad"] * df["precio"]

# KPI 1: ventas totales
ventas_totales = df["total"].sum()

# KPI 2: producto más vendido
producto_mas_vendido = (
    df.groupby("producto")["cantidad"]
    .sum()
    .idxmax()
)

# Guardar resumen
with open("resultados/resumen.txt", "w") as f:
    f.write(f"Ventas totales: ${ventas_totales}\\n")
    f.write(f"Producto más vendido: {producto_mas_vendido}\\n")

# Gráfico
ventas_producto = df.groupby("producto")["cantidad"].sum()

ventas_producto.plot(kind="bar")
plt.title("Cantidad vendida por producto")
plt.tight_layout()

plt.savefig("resultados/grafico_ventas.png")

print("Análisis completado")
