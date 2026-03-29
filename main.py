import os
import pandas as pd
import psycopg2
from dotenv import load_dotenv

# 1. Cargar configuración
load_dotenv()
db_url = os.getenv("DB_URL")

def iniciar_app():
    print("--- Iniciando Aplicación de Gestión de Datos para IA ---")
    
    # 2. Datos de rendimiento de un modelo de IA
    data = {'metrica': ['Exactitud', 'Precision', 'Recall'], 'valor': [0.95, 0.92, 0.88]}
    df = pd.DataFrame(data)
    print("Resultados del modelo procesados localmente:")
    print(df)
    
    # 3. Persistencia en la nube (Supabase)
    if db_url:
        try:
            # Conexión a la base de datos
            conn = psycopg2.connect(db_url)
            cur = conn.cursor()
            
            # Crear tabla si no existe
            cur.execute("CREATE TABLE IF NOT EXISTS metricas_ia (metrica TEXT, valor FLOAT);")
            
            # Insertar los datos del DataFrame
            for index, row in df.iterrows():
                cur.execute("INSERT INTO metricas_ia (metrica, valor) VALUES (%s, %s)", (row['metrica'], row['valor']))
            
            conn.commit()
            print("✅ ¡Éxito! Los datos han sido persistidos en Supabase.")
            cur.close()
            conn.close()
        except Exception as e:
            print(f" Error al conectar o insertar en la base de datos: {e}")
    else:
        print(" Advertencia: No se encontró DB_URL en el entorno.")

if __name__ == "__main__":
    iniciar_app()