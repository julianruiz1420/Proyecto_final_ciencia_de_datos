# cargar_datos.py
#cambiar la ruta del csv

# se crea una función para cargar los datos para que permita ser llamada en otros scrip del proyecto.

import pandas as pd
from pathlib import Path

def cargar_df_ppal():
    
    ruta_csv = Path(r"D:\3_Especialización_en_ciencia_de_datos\2. material de clase, cursos y materias\ciencia de datos\Proyecto_final_chrum\data\Churn_Modelling.csv")
    
    if not ruta_csv.exists():
        raise FileNotFoundError(f"No se encontró el archivo en: {ruta_csv}")
    
    return pd.read_csv(ruta_csv)


