from pathlib import Path
import pandas as pd

# Construir ruta relativa al archivo CSV
ruta_csv = Path("Churn_Modelling/Churn_Modelling.csv")

# Cargar el CSV
df_ppal = pd.read_csv(ruta_csv)
print(df_ppal.head())


print(df_ppal.head)

print(df_ppal.describe())
print(df_ppal.info())