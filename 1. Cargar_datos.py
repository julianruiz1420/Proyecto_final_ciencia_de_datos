# Cambiar la dirección donde este alojada el csv

import pandas as pd


Url_csv = (r"D:\3_Especialización_en_ciencia_de_datos\2. material de clase, cursos y materias\ciencia de datos\Proyecto_final_chrum\data\Churn_Modelling.csv")
           
df_ppal = pd.read_csv(Url_csv)

print(df_ppal.head)

print(df_ppal.describe())

print(df_ppal.info())   

