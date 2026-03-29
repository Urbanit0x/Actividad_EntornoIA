import os
import pandas as pd
from dotenv import load_dotenv

# 1. Cargar configuración (Estrategia de variables de entorno)
load_dotenv()
db_url = os.getenv("DB_URL")

def iniciar_app():
    print("--- Iniciando Aplicación de Datos ---")
    
    # 2. Simular datos de entrada (IA/Data Analysis)
    data = {'parametro': ['Exactitud', 'Precision', 'Recall'], 'valor': [0.95, 0.92, 0.88]}
    df = pd.DataFrame(data)
    
    print("Datos procesados listos para la nube:")
    print(df)
    
    if db_url:
        print(f"Conexión establecida con Supabase en: {db_url[:15]}...")
    else:
        print("Advertencia: No se encontró DB_URL. Revisa tu archivo .env")

if __name__ == "__main__":
    iniciar_app()