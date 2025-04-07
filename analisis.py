

from cargar_datos import cargar_df_ppal

df_ppal = cargar_df_ppal()

print(df_ppal.head())

print(df_ppal.describe())
print(df_ppal.info())