import pytest
import pymysql

# Testovací konfigurace databáze
TEST_DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "02112008@*",  # upravte dle konfigurace
    "database": "test_task_manager_db",
    "charset": "utf8mb4"
}

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

