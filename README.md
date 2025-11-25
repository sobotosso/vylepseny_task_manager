# Vylepšený Správce Úkolů

Aplikace pro správu úkolů s MySQL databázovým backendem. Umožňuje uživatelům vytvářet, zobrazovat, aktualizovat a mazat úkoly prostřednictvím jednoduchého textového rozhraní.

## Obsah

- [Funkce](#-funkce)
- [Požadavky](#-požadavky)
- [Instalace](#-instalace)
- [Konfigurace](#-konfigurace)
- [Použití](#-použití)
- [Struktura databáze](#-struktura-databáze)
- [Popis funkcí](#-popis-funkcí)

## Funkce

- **Přidávání úkolů** - Vytváření nových úkolů s názvem, popisem a automatickým nastavením stavu
- **Zobrazení úkolů** - Zobrazení všech aktivních úkolů (Nezahájeno, Probíhá)
- **Aktualizace úkolů** - Změna stavu úkolu (Probíhá/Hotovo)
- **Mazání úkolů** - Odstranění úkolů s potvrzením
- **Automatická inicializace** - Automatické vytvoření databáze a tabulky při prvním spuštění
- **Ošetření chyb** - Robustní zpracování chyb při práci s databází

## Požadavky

- Python 3.6 nebo vyšší
- MySQL Server (lokálně nebo vzdáleně)
- PyMySQL (Python MySQL klient)

## Instalace

### 1. Příprava prostředí

**Přesuňte se do složky projektu:**
```bash
cd Projektove_ukoly/vylepseny_task_manager
```

**Aktivujte virtuální prostředí (venv):**

Na macOS/Linux:
```bash
source venv/bin/activate
```

Na Windows:
```bash
venv\Scripts\activate
```

Po aktivaci byste měli vidět `(venv)` na začátku příkazové řádky.

### 2. Instalace závislostí

**Nainstalujte všechny potřebné balíčky:**
```bash
pip install -r requirements.txt
```

Tím se nainstalují:
- `PyMySQL` - pro připojení k MySQL databázi (řeší problémy s autentizačními pluginy)
- `pytest` - pro spouštění testů
- `python-dotenv` - pro načítání konfigurace z `.env` souboru

### 3. Kontrola MySQL Serveru

**Ujistěte se, že máte spuštěný MySQL Server** na vašem počítači.

### 4. Konfigurace databáze

Vytvořte soubor `.env` v kořenovém adresáři projektu a nastavte parametry připojení k databázi (viz sekce Konfigurace níže).

## Konfigurace

Před spuštěním aplikace je nutné vytvořit soubor `.env` s parametry připojení k databázi:

1. **Zkopírujte šablonu:**
   ```bash
   cp .env.example .env
   ```

2. **Upravte soubor `.env`** a vyplňte své údaje:
   ```env
   DB_HOST=localhost
   DB_USER=root
   DB_PASSWORD=vaše_heslo
   DB_DATABASE=task_manager_db
   TEST_DB_DATABASE=test_task_manager_db
   ```

**Důležité:** 
- Soubor `.env` je v `.gitignore`, takže se necommitne do gitu
- Před použitím změňte heslo na bezpečné heslo pro vaši databázi
- Pokud soubor `.env` neexistuje, aplikace použije výchozí hodnoty

## Struktura projektu

Projekt je organizován podle doporučených postupů pro Python projekty s testy:

```
vylepseny_task_manager/
├── src/                    # Zdrojový kód aplikace
│   ├── __init__.py
│   ├── db.py              # Databázové funkce
│   └── task_manager.py    # Hlavní logika aplikace
├── tests/                  # Testy
│   ├── __init__.py
│   ├── conftest.py        # Pytest fixtures
│   └── test_task_manager.py  # Testy aplikace
├── script.py              # Hlavní vstupní bod aplikace
├── requirements.txt       # Závislosti projektu
├── .env.example           # Šablona pro konfiguraci (.env)
├── .env                   # Konfigurace databáze (není v gitu)
└── README.md              # Tato dokumentace
```

## Spuštění aplikace

**Důležité:** Před spuštěním aplikace se ujistěte, že:
1. ✅ Máte aktivované virtuální prostředí (`venv`)
2. ✅ Máte nainstalované závislosti (`pip install -r requirements.txt`)
3. ✅ MySQL Server je spuštěný
4. ✅ Máte vytvořený a správně nakonfigurovaný soubor `.env` s přihlašovacími údaji

**Spuštění aplikace:**
```bash
python script.py
```

Nebo:
```bash
python3 script.py
```

## Spuštění testů

**Důležité:** Před spuštěním testů se ujistěte, že:
1. ✅ Máte aktivované virtuální prostředí (`venv`)
2. ✅ Máte nainstalované závislosti (včetně `pytest` a `cryptography`)
3. ✅ MySQL Server je spuštěný
4. ✅ Máte vytvořený soubor `.env` s konfigurací (testy používají testovací databázi `test_task_manager_db`)

**Základní spuštění testů:**
```bash
pytest
```

**S podrobnějším výstupem:**
```bash
pytest -v
```

**S velmi podrobným výstupem:**
```bash
pytest -vv
```

**Spuštění konkrétního testu:**
```bash
pytest tests/test_task_manager.py::test_pridani_ukolu_positivni
```

**Spuštění testů s výpisem printů:**
```bash
pytest -s
```

**Důležité:** Testy automaticky vytvoří testovací databázi `test_task_manager_db` při prvním spuštění pomocí session-scoped fixture `setup_test_db()`.

## Rychlý start - Shrnutí kroků

```bash
# 1. Přejděte do složky projektu
cd Projektove_ukoly/vylepseny_task_manager

# 2. Aktivujte venv
source venv/bin/activate  # macOS/Linux
# nebo
venv\Scripts\activate    # Windows

# 3. Nainstalujte závislosti (pokud ještě nejsou nainstalované)
pip install -r requirements.txt

# 4. Spusťte aplikaci
python script.py

# 5. Nebo spusťte testy
pytest -v
```

## Deaktivace virtuálního prostředí

Po dokončení práce můžete deaktivovat venv příkazem:
```bash
deactivate
```

Po spuštění se zobrazí hlavní menu s následujícími možnostmi:

```
Správce úkolů
1. Přidat nový úkol
2. Zobrazit všechny úkoly
3. Aktualizovat úkol
4. Odstranit úkol
5. Konec programu
```

### Přidání nového úkolu (volba 1)
- Zadejte název úkolu (povinné)
- Zadejte popis úkolu (povinné)
- Úkol bude automaticky vytvořen se stavem "Nezahájeno" a aktuálním datem a časem

### Zobrazení úkolů (volba 2)
- Zobrazí se všechny aktivní úkoly (stav: Nezahájeno nebo Probíhá)
- Úkoly jsou seřazeny podle data vytvoření
- Zobrazí se ID, název, popis a stav každého úkolu

### Aktualizace úkolu (volba 3)
- Nejprve se zobrazí seznam všech úkolů s jejich ID
- Zadejte ID úkolu, který chcete aktualizovat
- Zadejte nový stav: "Probíhá" nebo "Hotovo"
- Úkol bude aktualizován

### Odstranění úkolu (volba 4)
- Nejprve se zobrazí seznam všech úkolů s jejich ID
- Zadejte ID úkolu, který chcete odstranit
- Potvrďte odstranění zadáním 'a' (ano) nebo 'n' (ne)
- Úkol bude trvale odstraněn z databáze

## Struktura databáze

Aplikace automaticky vytvoří databázi `task_manager_db` a tabulku `ukoly` s následující strukturou:

| Sloupec | Typ | Popis |
|---------|-----|-------|
| `id` | INT AUTO_INCREMENT PRIMARY KEY | Jedinečné ID úkolu |
| `nazev` | VARCHAR(255) NOT NULL | Název úkolu |
| `popis` | TEXT NOT NULL | Detailní popis úkolu |
| `stav` | ENUM('Nezahájeno','Probíhá','Hotovo') | Aktuální stav úkolu (výchozí: 'Nezahájeno') |
| `datum_vytvoreni` | DATETIME NOT NULL | Datum a čas vytvoření úkolu |

## Popis funkcí

### `pripojeni_db()`
Vytváří připojení k MySQL databázi na základě konfigurace z `.env` souboru. Vrací připojení nebo `None` v případě chyby.

### `vytvorit_db()`
Vytváří databázi `task_manager_db`, pokud ještě neexistuje. Připojuje se k MySQL serveru bez specifikace databáze.

### `vytvorit_tabulku_ukoly(conn)`
Vytváří tabulku `ukoly` v databázi, pokud ještě neexistuje. Přijímá aktivní připojení k databázi jako parametr.

### `pridat_ukol(conn)`
Interaktivní funkce pro přidání nového úkolu. Vyžaduje název a popis úkolu (oba povinné). Automaticky nastaví stav na "Nezahájeno" a přidá aktuální datum a čas.

### `zobrazit_ukoly(conn)`
Zobrazí všechny aktivní úkoly (stav: Nezahájeno nebo Probíhá) seřazené podle data vytvoření. Zobrazí ID, název, popis a stav každého úkolu.

### `aktualizovat_ukol(conn)`
Umožňuje změnit stav existujícího úkolu. Nejprve zobrazí seznam všech úkolů, pak umožní výběr úkolu podle ID a změnu stavu na "Probíhá" nebo "Hotovo".

### `odstranit_ukol(conn)`
Umožňuje odstranit úkol z databáze. Zobrazí seznam úkolů, umožní výběr podle ID a vyžaduje potvrzení před odstraněním.

### `hlavni_menu(conn)`
Hlavní smyčka aplikace, která zobrazuje menu a zpracovává uživatelské volby. Spouští příslušné funkce podle zvolené možnosti.

## 🔒 Bezpečnost

- **Heslo databáze:** Ujistěte se, že máte silné heslo pro MySQL uživatele
- **Konfigurace v .env:** Přihlašovací údaje jsou uloženy v `.env` souboru, který není commitován do gitu
- **SQL Injection:** Aplikace používá parametrizované dotazy pro ochranu před SQL injection
- **Validace vstupů:** Aplikace validuje všechny uživatelské vstupy před zpracováním

## ⚠️ Poznámky

- Aplikace automaticky vytvoří databázi a tabulku při prvním spuštění
- Hotové úkoly (stav: "Hotovo") se nezobrazují v seznamu aktivních úkolů
- Odstranění úkolu je trvalé a nelze ho vrátit zpět
- Datum vytvoření se ukládá automaticky při přidání úkolu

## 🐛 Řešení problémů

**Chyba připojení k databázi:**
- Ověřte, že MySQL server běží
- Zkontrolujte správnost přihlašovacích údajů v souboru `.env`
- Ujistěte se, že soubor `.env` existuje a obsahuje všechny potřebné proměnné
- Ujistěte se, že má uživatel oprávnění k vytváření databází

**Chyba při vytváření tabulky:**
- Ověřte, že má uživatel oprávnění k vytváření tabulek
- Zkontrolujte, zda databáze existuje

## 📝 Detailní popis skriptu `script.py`

Hlavní vstupní bod aplikace, který inicializuje databázi a spouští hlavní menu.

### Struktura skriptu:

```python
from src.db import vytvorit_db, pripojeni_db, vytvorit_tabulku_ukoly
from src.task_manager import hlavni_menu

if __name__ == "__main__":
    vytvorit_db()                    # 1. Vytvoří databázi, pokud neexistuje
    connection = pripojeni_db()       # 2. Připojí se k databázi
    if connection:
        vytvorit_tabulku_ukoly(connection)  # 3. Vytvoří tabulku, pokud neexistuje
        hlavni_menu(connection)       # 4. Spustí hlavní menu aplikace
        connection.close()           # 5. Uzavře připojení po ukončení
    else:
        print("Nepodařilo se připojit k databázi, program končí.")
```

### Krok za krokem:

1. **`vytvorit_db()`** - Vytvoří databázi `task_manager_db`, pokud ještě neexistuje. Připojuje se k MySQL serveru bez specifikace konkrétní databáze.

2. **`pripojeni_db()`** - Vytvoří připojení k databázi na základě konfigurace z `.env` souboru. Vrací připojení nebo `None` v případě chyby.

3. **`vytvorit_tabulku_ukoly(connection)`** - Vytvoří tabulku `ukoly` v databázi, pokud ještě neexistuje. Struktura tabulky je definována v této funkci.

4. **`hlavni_menu(connection)`** - Spustí interaktivní hlavní menu aplikace, které umožňuje uživateli pracovat s úkoly.

5. **`connection.close()`** - Po ukončení aplikace uzavře připojení k databázi.

### Spuštění:

Skript se spouští příkazem:
```bash
python script.py
```

Nebo s explicitním Python interpretem:
```bash
python3 script.py
```

**Poznámka:** Skript musí být spuštěn z kořenového adresáře projektu, aby správně našel moduly v `src/` a načetl `.env` soubor.

## 🧪 Detailní popis testů

Projekt obsahuje komplexní testovací sadu pro ověření funkcionality aplikace.

### Struktura testů

Testy jsou umístěny v `tests/test_task_manager.py` a používají pytest framework s fixture z `tests/conftest.py`.

### Testovací konfigurace (`tests/conftest.py`)

#### Fixtures:

1. **`setup_test_db()`** (session-scoped, autouse=True)
   - Automaticky se spustí před všemi testy
   - Vytvoří testovací databázi `test_task_manager_db`, pokud neexistuje
   - Spouští se pouze jednou za celou test session

2. **`db_connection()`** (function-scoped)
   - Vytvoří nové připojení k testovací databázi pro každý test
   - Vytvoří tabulku `ukoly`, pokud neexistuje
   - Po dokončení testu vyčistí tabulku pomocí `TRUNCATE TABLE ukoly`
   - Vrací tuple `(conn, cursor)` pro použití v testech

### Testovací funkce (`tests/test_task_manager.py`)

#### Pomocné funkce pro testy:

- **`pridat_ukol_db(cursor, conn, nazev, popis)`** - Přidá úkol do databáze
- **`aktualizovat_ukol_db(cursor, conn, id_ukolu, novy_stav)`** - Aktualizuje stav úkolu
- **`odstranit_ukol_db(cursor, conn, id_ukolu)`** - Odstraní úkol z databáze

#### Testy:

1. **`test_pridani_ukolu_positivni`**
   - **Účel:** Ověřuje úspěšné přidání úkolu s platnými daty
   - **Kroky:** Přidá úkol s názvem "Test úkol" a popisem "Popis úkolu"
   - **Očekávání:** Úkol je v databázi (COUNT = 1)

2. **`test_pridani_ukolu_negativni`**
   - **Účel:** Ověřuje validaci při přidání úkolu s prázdným názvem
   - **Kroky:** Pokusí se přidat úkol s prázdným názvem
   - **Očekávání:** Vyvolá `ValueError` s hláškou "Název úkolu nesmí být prázdný"

3. **`test_pridani_ukolu_negativni_popis`**
   - **Účel:** Ověřuje validaci při přidání úkolu s prázdným popisem
   - **Kroky:** Pokusí se přidat úkol s prázdným popisem
   - **Očekávání:** Vyvolá `ValueError` s hláškou "Popis úkolu nesmí být prázdný"

4. **`test_aktualizace_ukolu_positivni`**
   - **Účel:** Ověřuje úspěšnou aktualizaci stavu úkolu
   - **Kroky:** 
     - Přidá úkol "Úkol k aktualizaci"
     - Získá jeho ID
     - Aktualizuje stav na "Hotovo"
   - **Očekávání:** Stav úkolu je změněn na "Hotovo"

5. **`test_aktualizace_ukolu_negativni`**
   - **Účel:** Ověřuje validaci při pokusu o nastavení neplatného stavu
   - **Kroky:** 
     - Přidá úkol
     - Pokusí se nastavit neplatný stav "Neplatný stav"
   - **Očekávání:** Vyvolá `ValueError` s hláškou "Neplatný stav"

6. **`test_odstraneni_ukolu_positivni`**
   - **Účel:** Ověřuje úspěšné odstranění úkolu
   - **Kroky:** 
     - Přidá úkol "Úkol k odstranění"
     - Získá jeho ID
     - Odstraní úkol
   - **Očekávání:** Úkol již není v databázi (COUNT = 0)

7. **`test_odstraneni_ukolu_negativni`**
   - **Účel:** Ověřuje chování při pokusu o odstranění neexistujícího úkolu
   - **Kroky:** Pokusí se odstranit úkol s ID 999999 (který neexistuje)
   - **Očekávání:** Operace proběhne bez chyby, ale úkol nebude odstraněn (tabulka zůstane prázdná)

### Spuštění testů

**Všechny testy:**
```bash
pytest tests/test_task_manager.py -v
```

**Konkrétní test:**
```bash
pytest tests/test_task_manager.py::test_pridani_ukolu_positivni -v
```

**S výpisem printů:**
```bash
pytest tests/test_task_manager.py -v -s
```

**S pokrytím kódu (pokud máte pytest-cov):**
```bash
pytest tests/test_task_manager.py --cov=src --cov-report=html
```

### Izolace testů

Každý test je izolovaný:
- Každý test dostane nové připojení k databázi
- Po každém testu se tabulka `ukoly` vyčistí pomocí `TRUNCATE TABLE`
- Testy mohou běžet v libovolném pořadí
- Testy neovlivňují navzájem svá data

### Testovací databáze

- Testy používají samostatnou testovací databázi `test_task_manager_db` (definovanou v `.env` jako `TEST_DB_DATABASE`)
- Tato databáze se automaticky vytvoří při prvním spuštění testů
- Produkční databáze `task_manager_db` není ovlivněna testy

## 📄 Licence

Tento projekt je vytvořen pro vzdělávací účely.
