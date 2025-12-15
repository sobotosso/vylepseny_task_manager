import pytest
import mysql.connector
import pymysql
from pymysql import Error
from datetime import datetime

DB_CONFIG = {
    "host": "localhost",
    "user": "", # vyplnit uživatelské jméno
    "password": "", #vyplnit heslo
    "database": "test_task_manager_db"
}

@pytest.fixture(scope="function")
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

@pytest.fixture(scope="function")
def db_connection(vytvorit_db):
    conn = mysql.connector.connect(**DB_CONFIG)
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
    cursor.execute("TRUNCATE TABLE ukoly")
    conn.commit()
    cursor.close()
    conn.close()

def pridat_ukol_db(cursor, conn, nazev, popis):
    if not nazev.strip():
        raise ValueError("Název úkolu nesmí být prázdný")
    if not popis.strip():
        raise ValueError("Popis úkolu nesmí být prázdný")
    datum = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    sql = "INSERT INTO ukoly (nazev, popis, stav, datum_vytvoreni) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (nazev, popis, 'Nezahájeno', datum))
    conn.commit()

def aktualizovat_ukol_db(cursor, conn, id_ukolu, novy_stav):
    if novy_stav not in ['Probíhá', 'Hotovo']:
        raise ValueError("Neplatný stav")
    cursor.execute("UPDATE ukoly SET stav = %s WHERE id = %s", (novy_stav, id_ukolu))
    conn.commit()

def odstranit_ukol_db(cursor, conn, id_ukolu):
    cursor.execute("DELETE FROM ukoly WHERE id = %s", (id_ukolu,))
    conn.commit()

# --- TESTY ---

def test_pridani_ukolu_positivni(db_connection):
    conn, cursor = db_connection
    pridat_ukol_db(cursor, conn, "Test úkol", "Popis úkolu")
    cursor.execute("SELECT COUNT(*) FROM ukoly WHERE nazev='Test úkol'")
    assert cursor.fetchone()[0] == 1

def test_pridani_ukolu_negativni(db_connection):
    conn, cursor = db_connection
    with pytest.raises(ValueError):
        pridat_ukol_db(cursor, conn, "", "Popis")

def test_pridani_ukolu_negativni_popis(db_connection):
    conn, cursor = db_connection
    with pytest.raises(ValueError):
        pridat_ukol_db(cursor, conn, "Nějaký název", "")

def test_aktualizace_ukolu_positivni(db_connection):
    conn, cursor = db_connection
    pridat_ukol_db(cursor, conn, "Úkol k aktualizaci", "Popis")
    cursor.execute("SELECT id FROM ukoly WHERE nazev='Úkol k aktualizaci'")
    id_ukolu = cursor.fetchone()[0]
    aktualizovat_ukol_db(cursor, conn, id_ukolu, "Hotovo")
    cursor.execute("SELECT stav FROM ukoly WHERE id=%s", (id_ukolu,))
    assert cursor.fetchone()[0] == "Hotovo"

def test_aktualizace_ukolu_negativni(db_connection):
    conn, cursor = db_connection
    pridat_ukol_db(cursor, conn, "Úkol nevalidní stav", "Popis")
    cursor.execute("SELECT id FROM ukoly WHERE nazev='Úkol nevalidní stav'")
    id_ukolu = cursor.fetchone()[0]
    with pytest.raises(ValueError):
        aktualizovat_ukol_db(cursor, conn, id_ukolu, "Neplatný stav")

def test_odstraneni_ukolu_positivni(db_connection):
    conn, cursor = db_connection
    pridat_ukol_db(cursor, conn, "Úkol k odstranění", "Popis")
    cursor.execute("SELECT id FROM ukoly WHERE nazev='Úkol k odstranění'")
    id_ukolu = cursor.fetchone()[0]
    odstranit_ukol_db(cursor, conn, id_ukolu)
    cursor.execute("SELECT COUNT(*) FROM ukoly WHERE id=%s", (id_ukolu,))
    assert cursor.fetchone()[0] == 0

def test_odstraneni_ukolu_negativni(db_connection):
    conn, cursor = db_connection
    odstranit_ukol_db(cursor, conn, 999999)
    cursor.execute("SELECT COUNT(*) FROM ukoly")
    assert cursor.fetchone()[0] == 0