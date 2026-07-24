import pandas as pd
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
from config import (
    SNOWFLAKE_USER,
    SNOWFLAKE_PASSWORD,
    SNOWFLAKE_ACCOUNT,
    SNOWFLAKE_WAREHOUSE,
    SNOWFLAKE_DATABASE,
    SNOWFLAKE_SCHEMA,
    SNOWFLAKE_ROLE,
    RAW_DATA_DIR,
    FILES_TO_TABLES
)

def get_snowflake_connection():
    return snowflake.connector.connect(
        user=SNOWFLAKE_USER,
        password=SNOWFLAKE_PASSWORD,
        account=SNOWFLAKE_ACCOUNT,
        warehouse=SNOWFLAKE_WAREHOUSE,
        database=SNOWFLAKE_DATABASE,
        schema=SNOWFLAKE_SCHEMA,
        role=SNOWFLAKE_ROLE
    )

def setup_snowflake_environment(conn):
    cursor = conn.cursor()
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {SNOWFLAKE_DATABASE};")
        cursor.execute(f"USE DATABASE {SNOWFLAKE_DATABASE};")
        cursor.execute(f"CREATE SCHEMA IF NOT EXISTS {SNOWFLAKE_SCHEMA};")
        cursor.execute(f"USE SCHEMA {SNOWFLAKE_SCHEMA};")
    finally:
        cursor.close()

def load_raw_data_to_bronze():
    print("🔌 Connexion b Snowflake...")
    conn = get_snowflake_connection()
    
    try:
        setup_snowflake_environment(conn)
        print("🚀 Re-ingestion Snowflake (Couche BRONZE)...")

        for file_name, table_name in FILES_TO_TABLES.items():
            file_path = RAW_DATA_DIR / file_name
            
            if not file_path.exists():
                print(f"⚠️ Fichier introuvable : {file_path}")
                continue

            print(f"📦 Chargement de {file_name} f {SNOWFLAKE_DATABASE}.{SNOWFLAKE_SCHEMA}.{table_name}...")
            
            df = pd.read_csv(file_path)
            
            # 🔴 IMPORTANT: Convertir tous les noms de colonnes en MAJUSCULES
            df.columns = [col.upper() for col in df.columns]
            df["_INGESTED_AT"] = pd.Timestamp.now()

            # Drop table if exists باش t-recréa b UPPERCASE clean
            cursor = conn.cursor()
            cursor.execute(f"DROP TABLE IF EXISTS {SNOWFLAKE_DATABASE}.{SNOWFLAKE_SCHEMA}.{table_name};")
            cursor.close()

            # write_pandas with UPPERCASE columns
            success, nchunks, nrows, _ = write_pandas(
                conn=conn,
                df=df,
                table_name=table_name,
                database=SNOWFLAKE_DATABASE,
                schema=SNOWFLAKE_SCHEMA,
                auto_create_table=True,
                quote_identifiers=False  # 🟢 Force Unquoted Uppercase in Snowflake
            )
            
            if success:
                print(f"✅ {nrows} lignes ajoutées dans la table{table_name}")
            else:
                print(f"❌ Erreur lors de l'insertion dans la table {table_name}")

        print("🎉 Ingestion terminée avec succès dans Snowflake!")

    finally:
        conn.close()

if __name__ == "__main__":
    load_raw_data_to_bronze()