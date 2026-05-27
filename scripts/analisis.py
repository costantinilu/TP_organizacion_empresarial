import pandas as pd

df = pd.read_csv("../datos/datos.csv")

print(df.describe())

df.describe().to_csv("../resultados/resumen.csv")
