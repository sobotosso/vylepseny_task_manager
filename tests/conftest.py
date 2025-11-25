import pytest
import pymysql
from pymysql import Error
import os
from dotenv import load_dotenv

# Načtení proměnných z .env souboru
load_dotenv()

# Testovací konfigurace databáze z .env souboru
TEST_DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", ""),
    "database": os.getenv("TEST_DB_DATABASE", "test_task_manager_db"),
    "charset": "utf8mb4"
}

def vytvorit_test_db():
    """Vytvoří testovací databázi, pokud neexistuje."""
    try:
        # Pro vytvoření databáze nepotřebujeme parametr database
        conn_config = {k: v for k, v in TEST_DB_CONFIG.items() if k != "database"}
        conn = pymysql.connect(**conn_config)
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {TEST_DB_CONFIG['database']}")
        conn.commit()
        cursor.close()
        conn.close()
    except Error as err:
        print(f"Chyba při vytváření testovací DB: {err}")

@pytest.fixture(scope="session", autouse=True)
def setup_test_db():
    """Session-scoped fixture pro vytvoření testovací databáze před všemi testy."""
    vytvorit_test_db()
    yield

@pytest.fixture(scope="function")
def db_connection():
    """Fixture pro vytvoření testovací databázové připojení a tabulky."""
    conn = pymysql.connect(**TEST_DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ukoly (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nazev VARCHAR(255) NOT NULL,
        popis TEXT NOT NULL,
        stav ENUM('Nezahájeno','Probíhá','Hotovo') NOT NULL DEFAULT 'Nezahájeno',
        datum_vytvoreni DATETIME NOT NULL
    )
    """)
    conn.commit()
    yield conn, cursor
    # Cleanup - vyčistit tabulku po každém testu
    cursor.execute("TRUNCATE TABLE ukoly")
    conn.commit()
    cursor.close()
    conn.close()

