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

### 3. Kontrola MySQL Serveru

**Ujistěte se, že máte spuštěný MySQL Server** na vašem počítači.

### 4. Konfigurace databáze

Upravte parametry připojení v souboru `src/db.py` (viz sekce Konfigurace níže).

## Konfigurace

Před spuštěním aplikace je nutné upravit parametry připojení k databázi v souboru `src/db.py`:

```python
DB_CONFIG = {
    "host": "localhost",      # Adresa MySQL serveru
    "user": "root",           # Uživatelské jméno
    "password": "02112008@*", # Heslo (UPRAVTE!)
    "database": "task_manager_db"  # Název databáze
}
```

**Důležité:** Před použitím změňte heslo na bezpečné heslo pro vaši databázi!

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
└── README.md              # Tato dokumentace
```

## Spuštění aplikace

**Důležité:** Před spuštěním aplikace se ujistěte, že:
1. ✅ Máte aktivované virtuální prostředí (`venv`)
2. ✅ Máte nainstalované závislosti (`pip install -r requirements.txt`)
3. ✅ MySQL Server je spuštěný
4. ✅ Máte správně nakonfigurované přihlašovací údaje v `src/db.py`

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
2. ✅ Máte nainstalované závislosti (včetně `pytest`)
3. ✅ MySQL Server je spuštěný
4. ✅ Testy používají testovací databázi `test_task_manager_db` (konfigurace v `tests/conftest.py`)

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
Vytváří připojení k MySQL databázi na základě konfigurace v `DB_CONFIG`. Vrací připojení nebo `None` v případě chyby.

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
- Zkontrolujte správnost přihlašovacích údajů v `DB_CONFIG`
- Ujistěte se, že má uživatel oprávnění k vytváření databází

**Chyba při vytváření tabulky:**
- Ověřte, že má uživatel oprávnění k vytváření tabulek
- Zkontrolujte, zda databáze existuje

## 📄 Licence

Tento projekt je vytvořen pro vzdělávací účely.
