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
- MySQL Connector pro Python

## Instalace

1. **Naklonujte nebo stáhněte projekt**

2. **Nainstalujte závislosti:**
```bash
pip install -r requirements.txt
```

3. **Ujistěte se, že máte spuštěný MySQL Server**

## Konfigurace

Před spuštěním aplikace je nutné upravit parametry připojení k databázi v souboru `script.py`:

```python
DB_CONFIG = {
    "host": "localhost",      # Adresa MySQL serveru
    "user": "root",           # Uživatelské jméno
    "password": "02112008@*", # Heslo (UPRAVTE!)
    "database": "task_manager_db"  # Název databáze
}
```

**Důležité:** Před použitím změňte heslo na bezpečné heslo pro vaši databázi!

## Použití

Spusťte aplikaci příkazem:

```bash
python script.py
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
