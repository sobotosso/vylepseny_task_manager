import pymysql
from pymysql import Error

# Parametry připojení k databázi
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "02112008@*",  # upravte dle konfigurace
    "database": "task_manager_db",
    "charset": "utf8mb4"
}

# Připojení k databázi s ošetřením chyb
def pripojeni_db():
    try:
        conn = pymysql.connect(**DB_CONFIG)
        return conn
    except Error as err:
        print(f"Chyba při připojování k DB: {err}")
    return None

# Vytvoření databáze pokud neexistuje
def vytvorit_db():
    try:
        # Pro vytvoření databáze nepotřebujeme parametr database
        conn_config = {k: v for k, v in DB_CONFIG.items() if k != "database"}
        conn = pymysql.connect(**conn_config)
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_CONFIG['database']}")
        conn.commit()
        cursor.close()
        conn.close()
    except Error as err:
        print(f"Chyba při vytváření DB: {err}")

# Vytvoření tabulky úkolů pokud neexistuje
def vytvorit_tabulku_ukoly(conn):
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS ukoly (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nazev VARCHAR(255) NOT NULL,
                popis TEXT NOT NULL,
                stav ENUM('Nezahájeno','Probíhá','Hotovo') NOT NULL DEFAULT 'Nezahájeno',
                datum_vytvoreni DATETIME NOT NULL
            )
            """
        )
        conn.commit()
        cursor.close()
    except Error as err:
        print(f"Chyba při vytváření tabulky: {err}")

