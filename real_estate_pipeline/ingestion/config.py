import os
from pathlib import Path
from dotenv import load_dotenv

# Charger les variables du fichier .env
env_path = Path(__file__).resolve().parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

# Configuration Snowflake
SNOWFLAKE_USER = os.getenv("SNOWFLAKE_USER", "ILHAM")
SNOWFLAKE_PASSWORD = os.getenv("SNOWFLAKE_PASSWORD")
SNOWFLAKE_ACCOUNT = os.getenv("SNOWFLAKE_ACCOUNT", "TEEDGDV-DE77206")
SNOWFLAKE_WAREHOUSE = os.getenv("SNOWFLAKE_WAREHOUSE", "COMPUTE_WH")
SNOWFLAKE_DATABASE = os.getenv("SNOWFLAKE_DATABASE", "FINANCE_DW")
SNOWFLAKE_SCHEMA = os.getenv("SNOWFLAKE_SCHEMA", "BRONZE")
SNOWFLAKE_ROLE = os.getenv("SNOWFLAKE_ROLE", "ACCOUNTADMIN")

# Chemins dial les CSV
RAW_DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "raw"

# Mapping dial les CSV vers les tables Snowflake
FILES_TO_TABLES = {
    "accounts.csv": "RAW_ACCOUNTS",
    "customers.csv": "RAW_CUSTOMERS",
    "loans.csv": "RAW_LOANS",
    "transactions.csv": "RAW_TRANSACTIONS"
}