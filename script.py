import mysql.connector
from mysql.connector import Error
from datetime import datetime

# Parametry připojení k databázi
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "02112008@*",  # upravte dle konfigurace
    "database": "task_manager_db"
}

# Připojení k databázi s ošetřením chyb
def pripojeni_db():
    try:
        conn = mysql.connector.connect(
            host=DB_CONFIG["host"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"],
            database=DB_CONFIG["database"]
        )
        if conn.is_connected():
            return conn
    except Error as err:
        print(f"Chyba při připojování k DB: {err}")
    return None

# Vytvoření databáze pokud neexistuje
def vytvorit_db():
    try:
        conn = mysql.connector.connect(
            host=DB_CONFIG["host"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"]
        )
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

def pridat_ukol(conn):
    while True:
        nazev_ukolu = input("Zadejte název úkolu: ").strip()
        if not nazev_ukolu:
            print("Název úkolu nesmí být prázdný")
            continue
        popis_ukolu = input("Zadejte popis úkolu: ").strip()
        if not popis_ukolu:
            print("Popis úkolu nesmí být prázdný")
            continue
        
        try:
            cursor = conn.cursor()
            datum = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            sql = "INSERT INTO ukoly (nazev, popis, stav, datum_vytvoreni) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (nazev_ukolu, popis_ukolu, 'Nezahájeno', datum))
            conn.commit()
            print(f"Úkol '{nazev_ukolu}' byl přidán.")
            cursor.close()
            break
        except Error as err:
            print(f"Chyba při přidávání úkolu: {err}")
            break

def zobrazit_ukoly(conn):
    try:
        cursor = conn.cursor()
        sql = "SELECT id, nazev, popis, stav FROM ukoly WHERE stav IN ('Nezahájeno', 'Probíhá') ORDER BY datum_vytvoreni"
        cursor.execute(sql)
        vysledky = cursor.fetchall()
        if not vysledky:
            print("Seznam úkolů je prázdný.")
        else:
            print("Seznam úkolů:")
            for radek in vysledky:
                print(f"{radek[0]}. {radek[1]} – {radek[2]}, Stav: {radek[3]}")
        cursor.close()
    except Error as err:
        print(f"Chyba při načítání úkolů: {err}")

def aktualizovat_ukol(conn):
    try:
        cursor = conn.cursor()
        # Zobrazit úkoly s ID, názvem a stavem pro výběr
        cursor.execute("SELECT id, nazev, stav FROM ukoly ORDER BY id")
        ukoly = cursor.fetchall()
        if not ukoly:
            print("Seznam úkolů je prázdný.")
            cursor.close()
            return
        
        print("Úkoly:")
        for u in ukoly:
            print(f"{u[0]}. {u[1]}, Stav: {u[2]}")

        while True:
            try:
                id_ukolu = int(input("Zadejte ID úkolu, který chcete aktualizovat: "))
                cursor.execute("SELECT id FROM ukoly WHERE id = %s", (id_ukolu,))
                if cursor.fetchone() is None:
                    print("Neplatné ID úkolu, zadejte znovu.")
                    continue
                break
            except ValueError:
                print("Musíte zadat platné číslo.")
        
        while True:
            novy_stav = input("Zadejte nový stav (Probíhá/Hotovo): ").strip()
            if novy_stav not in ['Probíhá', 'Hotovo']:
                print("Neplatný stav, zadejte znovu.")
                continue
            break
        
        cursor.execute("UPDATE ukoly SET stav = %s WHERE id = %s", (novy_stav, id_ukolu))
        conn.commit()
        print("Úkol byl aktualizován.")
        cursor.close()
    except Error as err:
        print(f"Chyba při aktualizaci úkolu: {err}")

def odstranit_ukol(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, nazev FROM ukoly ORDER BY id")
        ukoly = cursor.fetchall()
        if not ukoly:
            print("Seznam úkolů je prázdný.")
            cursor.close()
            return

        print("Úkoly:")
        for u in ukoly:
            print(f"{u[0]}. {u[1]}")
        
        while True:
            try:
                id_ukolu = int(input("Zadejte ID úkolu, který chcete odstranit: "))
                cursor.execute("SELECT id, nazev FROM ukoly WHERE id = %s", (id_ukolu,))
                vysledek = cursor.fetchone()
                if vysledek is None:
                    print("Neplatné ID úkolu, zadejte znovu.")
                    continue
                
                potvrzeni = input(f"Opravdu chcete odstranit úkol '{vysledek[1]}'? (a/n): ").strip().lower()
                if potvrzeni == 'a':
                    cursor.execute("DELETE FROM ukoly WHERE id = %s", (id_ukolu,))
                    conn.commit()
                    print(f"Úkol '{vysledek[1]}' byl odstraněn.")
                else:
                    print("Odstranění zrušeno.")
                break
            except ValueError:
                print("Musíte zadat platné číslo.")
        cursor.close()
    except Error as err:
        print(f"Chyba při odstraňování úkolu: {err}")

def hlavni_menu(conn):
    while True:
        print("\nSprávce úkolů")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Aktualizovat úkol")
        print("4. Odstranit úkol")
        print("5. Konec programu")

        volba = input("Vyberte možnost (1–5): ").strip()

        if volba == "1":
            pridat_ukol(conn)
        elif volba == "2":
            zobrazit_ukoly(conn)
        elif volba == "3":
            aktualizovat_ukol(conn)
        elif volba == "4":
            odstranit_ukol(conn)
        elif volba == "5":
            print("Konec programu.")
            break
        else:
            print("Zadali jste neplatnou volbu, zadejte volbu znovu.")

if __name__ == "__main__":
    vytvorit_db()
    connection = pripojeni_db()
    if connection:
        vytvorit_tabulku_ukoly(connection)
        hlavni_menu(connection)
        connection.close()
    else:
        print("Nepodařilo se připojit k databázi, program končí.")
