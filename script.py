import mysql.connector
from datetime import datetime

# nastaveni databaze podle lekce
host = "localhost"
database_name = "task_manager_db"
user = "root"
password = "02112008@*"

# globalni promenna pro pripojeni - podle lekce
conn = None


def pripojeni_db():
    # pripojeni k MySQL podle lekce 6
    global conn
    
    # nejdriv vytvorim databazi pokud neexistuje
    try:
        temp_conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        cursor = temp_conn.cursor()
        
        # zkontroluju jestli databaze existuje
        cursor.execute("SHOW DATABASES LIKE '" + database_name + "'")
        result = cursor.fetchone()
        
        if result == None:
            cursor.execute("CREATE DATABASE " + database_name)
            print("Databaze byla vytvorena.")
        else:
            print("Databaze jiz existuje.")
        
        cursor.close()
        temp_conn.close()
    except mysql.connector.Error as err:
        print("Chyba pri vytvareni databaze: " + str(err))
        return False
    
    # pripojeni k databazi
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database_name
        )
        cursor = conn.cursor()
        print("Připojení k databázi bylo úspěšné.")
        cursor.close()
        return True
    except mysql.connector.Error as err:
        print("Chyba při připojování: " + str(err))
        return False


def vytvoreni_tabulky():
    try:
        cursor = conn.cursor()
        
        # kontrola existence tabulky
        cursor.execute("SHOW TABLES LIKE 'ukoly'")
        result = cursor.fetchone()
        
        if result == None:
            # vytvoreni tabulky
            cursor.execute("""
                CREATE TABLE ukoly (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nazev VARCHAR(255) NOT NULL,
                    popis TEXT NOT NULL,
                    stav ENUM('nezahájeno', 'probíhá', 'hotovo') NOT NULL DEFAULT 'nezahájeno',
                    datum_vytvoreni DATETIME NOT NULL
                )
            """)
            conn.commit()
            print("Tabulka ukoly byla vytvorena.")
        else:
            print("Tabulka jiz existuje.")
        
        cursor.close()
        return True
    except mysql.connector.Error as err:
        print("Chyba při vytváření tabulky: " + str(err))
        return False


def pridat_ukol():
    while True:
        nazev_ukolu = input("Zadejte název úkolu: ").strip()
        if nazev_ukolu == "":
            print("Název úkolu nesmí být prázdný")
            continue

        popis_ukolu = input("Zadejte popis úkolu: ").strip()
        if popis_ukolu == "":
            print("Popis úkolu nesmí být prázdný")
            continue

        try:
            cursor = conn.cursor()
            datum_vytvoreni = datetime.now()
            sql = "INSERT INTO ukoly (nazev, popis, stav, datum_vytvoreni) VALUES ('" + nazev_ukolu + "', '" + popis_ukolu + "', 'nezahájeno', '" + str(datum_vytvoreni) + "')"
            cursor.execute(sql)
            conn.commit()
            print("Úkol '" + nazev_ukolu + "' byl přidán.")
            cursor.close()
            break
        except mysql.connector.Error as err:
            print("Chyba při přidávání úkolu: " + str(err))
            break


def zobrazit_ukoly():
    try:
        cursor = conn.cursor()
      
        cursor.execute("SELECT id, nazev, popis, stav, datum_vytvoreni FROM ukoly WHERE stav IN ('nezahájeno', 'probíhá') ORDER BY id")
        
        ukoly = cursor.fetchall()
        
        if len(ukoly) == 0:
            print("Seznam úkolů je prázdný.")
        else:
            print("\nSeznam úkolů:")
            print("=" * 60)
            for row in ukoly:
                id_ukolu = row[0]
                nazev = row[1]
                popis = row[2]
                stav = row[3]
                datum = row[4]
                
                print("ID: " + str(id_ukolu))
                print("Název: " + nazev)
                print("Popis: " + popis)
                print("Stav: " + stav)
                print("Datum: " + str(datum))
                print("-" * 60)
        
        cursor.close()
    except mysql.connector.Error as err:
        print("Chyba při načítání dat: " + str(err))


def zobrazit_vsechny_ukoly():
    # pomocna funkce pro zobrazeni vsech ukolu
    try:
        cursor = conn.cursor()
        
        cursor.execute("SELECT id, nazev, stav FROM ukoly ORDER BY id")
        ukoly = cursor.fetchall()
        
        if len(ukoly) == 0:
            print("Seznam úkolů je prázdný.")
            return False
        
        print("\nSeznam úkolů:")
        for row in ukoly:
            print("ID: " + str(row[0]) + " | Název: " + row[1] + " | Stav: " + row[2])
        
        cursor.close()
        return True
    except mysql.connector.Error as err:
        print("Chyba: " + str(err))
        return False


def aktualizovat_ukol():

    if not zobrazit_vsechny_ukoly():
        return
    
    try:
        id_ukolu = input("\nZadejte ID úkolu: ").strip()
        
        try:
            id_ukolu = int(id_ukolu)
        except:
            print("Musíte zadat číslo.")
            return
        
        cursor = conn.cursor()

        cursor.execute("SELECT id, stav FROM ukoly WHERE id = " + str(id_ukolu))
        ukol = cursor.fetchone()
        
        if ukol == None:
            print("Úkol s ID " + str(id_ukolu) + " neexistuje.")
            cursor.close()
            return
        
        print("\nAktuální stav: " + ukol[1])
        print("Vyberte nový stav:")
        print("1. Probíhá")
        print("2. Hotovo")
        
        volba = input("Vaše volba: ").strip()
        
        if volba == "1":
            novy_stav = "probíhá"
        elif volba == "2":
            novy_stav = "hotovo"
        else:
            print("Neplatná volba.")
            cursor.close()
            return
        
        cursor.execute("UPDATE ukoly SET stav = '" + novy_stav + "' WHERE id = " + str(id_ukolu))
        conn.commit()
        print("Stav úkolu byl změněn na: " + novy_stav)
        cursor.close()
        
    except mysql.connector.Error as err:
        print("Chyba při aktualizaci dat: " + str(err))


def odstranit_ukol():

    if not zobrazit_vsechny_ukoly():
        return
    
    try:
        id_ukolu = input("\nZadejte ID úkolu k odstranění: ").strip()
        
        try:
            id_ukolu = int(id_ukolu)
        except:
            print("Musíte zadat číslo.")
            return
        
        cursor = conn.cursor()
        
        cursor.execute("SELECT id, nazev FROM ukoly WHERE id = " + str(id_ukolu))
        ukol = cursor.fetchone()
        
        if ukol == None:
            print("Úkol s ID " + str(id_ukolu) + " neexistuje.")
            cursor.close()
            return
        
        cursor.execute("DELETE FROM ukoly WHERE id = " + str(id_ukolu))
        conn.commit()
        print("Záznam byl smazán.")
        
        cursor.close()
        
    except mysql.connector.Error as err:
        print("Chyba při mazání dat: " + str(err))


def hlavni_menu():
    while True:
        print("\nSprávce úkolů")
        print("1. Přidat úkol")
        print("2. Zobrazit úkoly")
        print("3. Aktualizovat úkol")
        print("4. Odstranit úkol")
        print("5. Ukončit program")

        volba = input("Vyberte možnost (1–5): ")

        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            aktualizovat_ukol()
        elif volba == "4":
            odstranit_ukol()
        elif volba == "5":
            print("Konec programu.")
            break
        else:
            print("Zadali jste neplatnou volbu, zadejte volbu znovu.")


# hlavni cast programu
print("Vylepšený správce úkolů")
#print("=" * 40)

# pripojeni k databazi
if not pripojeni_db():
    print("Nelze se pripojit k databazi.")
    exit()

# vytvoreni tabulky
if not vytvoreni_tabulky():
    print("Nelze vytvorit tabulku.")
    exit()

# spusteni menu
try:
    hlavni_menu()
finally:
    # uzavreni spojeni
    if conn != None and conn.is_connected():
        conn.close()
        print("\nPřipojení k databazi bylo ukonceno.")


