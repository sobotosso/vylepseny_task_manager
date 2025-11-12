# 📚 Návod na testování pro úplné začátečníky

Tento návod vás provede základy testování v Pythonu pomocí pytestu. Je určen pro úplné začátečníky, kteří nemají žádné zkušenosti s testováním ani s Pythonem.

## 📖 Obsah

1. [Co jsou testy a proč je psát?](#co-jsou-testy-a-proč-je-psát)
2. [Základy pytestu](#základy-pytestu)
3. [Struktura testovacího souboru](#struktura-testovacího-souboru)
4. [První jednoduchý test](#první-jednoduchý-test)
5. [Pozitivní vs. negativní testy](#pozitivní-vs-negativní-testy)
6. [Fixtures - sdílené prostředky](#fixtures---sdílené-prostředky)
7. [Testování databázových operací](#testování-databázových-operací)
8. [Krok za krokem - Vytvoření vlastního testu](#krok-za-krokem---vytvoření-vlastního-testu)
9. [Spouštění testů](#spouštění-testů)
10. [Časté chyby a jejich řešení](#časté-chyby-a-jejich-řešení)

---

## Co jsou testy a proč je psát?

### Co jsou testy?

**Testy** jsou malé programy, které automaticky kontrolují, zda váš kód funguje správně. Místo toho, abyste ručně spouštěli aplikaci a zkoušeli všechny možnosti, testy to udělají za vás.

### Příklad bez testů:
```
1. Spustíte aplikaci
2. Ručně přidáte úkol
3. Ručně zkontrolujete, jestli se úkol přidal
4. Ručně aktualizujete úkol
5. Ručně zkontrolujete, jestli se aktualizoval
... a tak dále pro každou funkci
```

### Příklad s testy:
```
1. Spustíte: pytest
2. Testy automaticky:
   - Přidají úkol
   - Zkontrolují, jestli se přidal
   - Aktualizují úkol
   - Zkontrolují, jestli se aktualizoval
   - A mnoho dalšího...
3. Dostanete zprávu: "Všechny testy prošly!" nebo "Test X selhal"
```

### Proč psát testy?

✅ **Automatizace** - Nemusíte ručně testovat každou funkci  
✅ **Rychlost** - Testy běží rychleji než ruční testování  
✅ **Spolehlivost** - Testy vždy testují stejně, bez chyb  
✅ **Odvaha měnit kód** - Když změníte kód, testy vám řeknou, jestli jste něco rozbili  
✅ **Dokumentace** - Testy ukazují, jak má kód fungovat  

---

## Základy pytestu

### Co je pytest?

**pytest** je knihovna (balíček) pro Python, která umožňuje psát a spouštět testy. Je to jeden z nejpopulárnějších nástrojů pro testování v Pythonu.

### Základní pravidla pro psaní testů v pytestu:

1. **Název souboru** musí začínat na `test_` (např. `test_task_manager.py`)
2. **Název funkce** musí začínat na `test_` (např. `test_pridani_ukolu`)
3. **Použijte `assert`** pro kontrolu výsledků

### Jednoduchý příklad:

```python
def test_scitani():
    """Test, který kontroluje, jestli 2 + 2 = 4"""
    vysledek = 2 + 2
    assert vysledek == 4  # Pokud je 4, test projde. Pokud ne, selže.
```

**Co se stane:**
- Pokud `vysledek == 4` → test **projde** ✅
- Pokud `vysledek != 4` → test **selže** ❌

---

## Struktura testovacího souboru

Podívejme se na strukturu vašeho testovacího souboru `tests/test_task_manager.py`:

```python
# 1. IMPORTOVÁNÍ - Načtení potřebných nástrojů
import pytest
from datetime import datetime

# 2. POMOCNÉ FUNKCE - Funkce, které testujeme
def pridat_ukol_db(cursor, conn, nazev, popis):
    # ... kód funkce ...
    pass

# 3. TESTY - Funkce, které testují náš kód
def test_pridani_ukolu_positivni(db_connection):
    # ... kód testu ...
    pass
```

### Části testovacího souboru:

1. **Importy** - Načteme potřebné nástroje (pytest, databázové moduly, atd.)
2. **Pomocné funkce** - Funkce, které chceme testovat (nebo jejich verze pro testování)
3. **Testy** - Funkce začínající na `test_`, které kontrolují, jestli náš kód funguje

---

## První jednoduchý test

Pojďme vytvořit úplně jednoduchý test, abyste pochopili základní principy:

### Test 1: Testování matematiky

Vytvořte soubor `tests/test_zaklady.py`:

```python
def test_scitani():
    """Test, který kontroluje sčítání"""
    vysledek = 2 + 2
    assert vysledek == 4

def test_nasobeni():
    """Test, který kontroluje násobení"""
    vysledek = 3 * 5
    assert vysledek == 15

def test_deleni():
    """Test, který kontroluje dělení"""
    vysledek = 10 / 2
    assert vysledek == 5
```

**Spusťte test:**
```bash
pytest tests/test_zaklady.py
```

**Výstup by měl být:**
```
tests/test_zaklady.py::test_scitani PASSED
tests/test_zaklady.py::test_nasobeni PASSED
tests/test_zaklady.py::test_deleni PASSED
```

### Test 2: Testování textu

```python
def test_text_velkymi():
    """Test, který kontroluje převod textu na velká písmena"""
    text = "ahoj"
    vysledek = text.upper()
    assert vysledek == "AHOJ"

def test_text_delka():
    """Test, který kontroluje délku textu"""
    text = "Python"
    delka = len(text)
    assert delka == 6
```

### Co je `assert`?

`assert` je klíčové slovo v Pythonu, které kontroluje, jestli je něco pravda:

```python
assert podminka  # Pokud je podmínka True, pokračuje se dál
                 # Pokud je False, test selže a vypíše chybu
```

**Příklady:**
```python
assert 5 > 3        # ✅ Projde (5 je větší než 3)
assert 2 == 2       # ✅ Projde (2 se rovná 2)
assert "a" == "b"   # ❌ Selže (a se nerovná b)
```

---

## Pozitivní vs. negativní testy

### Pozitivní testy (Happy Path)

**Pozitivní testy** kontrolují, jestli kód funguje správně, když mu dáte **správné vstupy**.

**Příklad:**
```python
def test_pridani_ukolu_positivni(db_connection):
    """Test přidání úkolu se správnými údaji"""
    conn, cursor = db_connection
    # Přidáme úkol se správnými údaji
    pridat_ukol_db(cursor, conn, "Test úkol", "Popis úkolu")
    
    # Zkontrolujeme, jestli se úkol přidal
    cursor.execute("SELECT COUNT(*) FROM ukoly WHERE nazev='Test úkol'")
    pocet = cursor.fetchone()[0]
    assert pocet == 1  # Očekáváme, že bude přesně 1 úkol
```

**Co testuje:**
- ✅ Pokud zadáme správný název a popis, úkol se přidá

### Negativní testy (Error Handling)

**Negativní testy** kontrolují, jestli kód správně **odmítne špatné vstupy** a vyhodí chybu.

**Příklad:**
```python
def test_pridani_ukolu_negativni(db_connection):
    """Test přidání úkolu s prázdným názvem - mělo by to selhat"""
    conn, cursor = db_connection
    
    # Zkusíme přidat úkol s prázdným názvem
    # Očekáváme, že to vyhodí chybu ValueError
    with pytest.raises(ValueError):
        pridat_ukol_db(cursor, conn, "", "Popis")
```

**Co testuje:**
- ✅ Pokud zadáme prázdný název, funkce vyhodí chybu `ValueError`

### Co je `pytest.raises()`?

`pytest.raises()` kontroluje, jestli kód vyhodí očekávanou chybu:

```python
with pytest.raises(ValueError):
    # Kód, který by měl vyhodit ValueError
    funkce_ktera_selze()
```

**Příklad:**
```python
def test_deleni_nulou():
    """Test, který kontroluje, jestli dělení nulou vyhodí chybu"""
    with pytest.raises(ZeroDivisionError):
        vysledek = 10 / 0  # Toto vyhodí ZeroDivisionError
```

---

## Fixtures - sdílené prostředky

### Co jsou fixtures?

**Fixtures** jsou funkce, které připravují něco pro testy. Místo toho, abyste v každém testu připravovali databázové připojení, vytvoříte fixture, která to udělá za vás.

### Příklad fixture v `tests/conftest.py`:

```python
@pytest.fixture(scope="function")
def db_connection():
    """Fixture pro vytvoření testovací databázové připojení"""
    # 1. PŘÍPRAVA - Vytvoříme připojení a tabulku
    conn = pymysql.connect(**TEST_DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS ukoly (...)")
    conn.commit()
    
    # 2. PŘEDÁNÍ - Předáme připojení testu
    yield conn, cursor
    
    # 3. ÚKLID - Po testu vyčistíme tabulku
    cursor.execute("TRUNCATE TABLE ukoly")
    conn.commit()
    cursor.close()
    conn.close()
```

### Jak používat fixture v testu?

Jednoduše přidejte název fixture jako parametr do testu:

```python
def test_pridani_ukolu_positivni(db_connection):
    # db_connection je automaticky předáno z fixture
    conn, cursor = db_connection
    # Teď můžeme použít conn a cursor
    pridat_ukol_db(cursor, conn, "Test úkol", "Popis")
```

### Co dělá `yield`?

`yield` rozděluje fixture na tři části:

1. **Před `yield`** - Příprava (vytvoření připojení, tabulky)
2. **`yield`** - Předání hodnoty testu
3. **Po `yield`** - Úklid (smazání dat, zavření připojení)

**Vizuálně:**
```
Test začíná
    ↓
Fixture: Příprava (před yield)
    ↓
Fixture: yield conn, cursor → Test dostane conn, cursor
    ↓
Test běží
    ↓
Test končí
    ↓
Fixture: Úklid (po yield)
```

### Proč používat fixtures?

✅ **DRY princip** - Don't Repeat Yourself (neopakujte se)  
✅ **Automatický úklid** - Data se automaticky smažou po každém testu  
✅ **Konzistence** - Všechny testy používají stejné prostředí  

---

## Testování databázových operací

### Jak testovat databázové operace?

Když testujete databázové operace, obvykle:

1. **Připravíte data** (vytvoříte úkol)
2. **Provedete operaci** (aktualizujete úkol)
3. **Zkontrolujete výsledek** (zkontrolujete, jestli se úkol aktualizoval)

### Příklad: Test přidání úkolu

```python
def test_pridani_ukolu_positivni(db_connection):
    """Test přidání úkolu do databáze"""
    conn, cursor = db_connection
    
    # 1. PŘIDÁME ÚKOL
    pridat_ukol_db(cursor, conn, "Test úkol", "Popis úkolu")
    
    # 2. ZKONTROLUJEME, ŽE SE ÚKOL PŘIDAL
    cursor.execute("SELECT COUNT(*) FROM ukoly WHERE nazev='Test úkol'")
    pocet = cursor.fetchone()[0]
    
    # 3. ASSERT - Očekáváme, že bude přesně 1 úkol
    assert pocet == 1
```

**Krok za krokem:**

1. `pridat_ukol_db(...)` - Přidá úkol do databáze
2. `cursor.execute(...)` - Spustí SQL dotaz, který spočítá úkoly s názvem "Test úkol"
3. `cursor.fetchone()[0]` - Získá výsledek (počet úkolů)
4. `assert pocet == 1` - Zkontroluje, jestli je počet roven 1

### Příklad: Test aktualizace úkolu

```python
def test_aktualizace_ukolu_positivni(db_connection):
    """Test aktualizace stavu úkolu"""
    conn, cursor = db_connection
    
    # 1. PŘIDÁME ÚKOL
    pridat_ukol_db(cursor, conn, "Úkol k aktualizaci", "Popis")
    
    # 2. NAJDEME ID ÚKOLU
    cursor.execute("SELECT id FROM ukoly WHERE nazev='Úkol k aktualizaci'")
    id_ukolu = cursor.fetchone()[0]  # Získáme ID (první sloupec)
    
    # 3. AKTUALIZUJEME ÚKOL
    aktualizovat_ukol_db(cursor, conn, id_ukolu, "Hotovo")
    
    # 4. ZKONTROLUJEME, ŽE SE ÚKOL AKTUALIZOVAL
    cursor.execute("SELECT stav FROM ukoly WHERE id=%s", (id_ukolu,))
    stav = cursor.fetchone()[0]
    
    # 5. ASSERT - Očekáváme, že stav je "Hotovo"
    assert stav == "Hotovo"
```

### Co je `fetchone()`?

`fetchone()` získává jeden řádek z výsledku SQL dotazu:

```python
cursor.execute("SELECT id, nazev FROM ukoly WHERE id=1")
radek = cursor.fetchone()
# radek je tuple: (1, "Název úkolu")
# radek[0] je ID: 1
# radek[1] je název: "Název úkolu"
```

---

## Krok za krokem - Vytvoření vlastního testu

Pojďme vytvořit nový test od začátku. Vytvoříme test, který zkontroluje, jestli se úkol správně přidá s výchozím stavem "Nezahájeno".

### Krok 1: Otevřete testovací soubor

Otevřete `tests/test_task_manager.py`

### Krok 2: Přidejte nový test

Na konec souboru přidejte:

```python
def test_ukol_ma_vychozi_stav(db_connection):
    """Test, který kontroluje, že nový úkol má výchozí stav 'Nezahájeno'"""
    conn, cursor = db_connection
    
    # 1. Přidáme úkol
    pridat_ukol_db(cursor, conn, "Nový úkol", "Popis nového úkolu")
    
    # 2. Najdeme úkol a zkontrolujeme jeho stav
    cursor.execute("SELECT stav FROM ukoly WHERE nazev='Nový úkol'")
    stav = cursor.fetchone()[0]
    
    # 3. Zkontrolujeme, že stav je "Nezahájeno"
    assert stav == "Nezahájeno"
```

### Krok 3: Spusťte test

```bash
pytest tests/test_task_manager.py::test_ukol_ma_vychozi_stav -v
```

### Krok 4: Zkontrolujte výsledek

Pokud test projde, uvidíte:
```
tests/test_task_manager.py::test_ukol_ma_vychozi_stav PASSED
```

### Cvičení: Vytvořte vlastní test

Zkuste vytvořit test, který:
1. Přidá úkol
2. Aktualizuje jeho stav na "Probíhá"
3. Zkontroluje, že stav je "Probíhá"

**Řešení:**
```python
def test_zmena_stavu_na_probiha(db_connection):
    """Test změny stavu úkolu na 'Probíhá'"""
    conn, cursor = db_connection
    
    # Přidáme úkol
    pridat_ukol_db(cursor, conn, "Úkol v práci", "Popis")
    
    # Najdeme ID
    cursor.execute("SELECT id FROM ukoly WHERE nazev='Úkol v práci'")
    id_ukolu = cursor.fetchone()[0]
    
    # Aktualizujeme stav
    aktualizovat_ukol_db(cursor, conn, id_ukolu, "Probíhá")
    
    # Zkontrolujeme stav
    cursor.execute("SELECT stav FROM ukoly WHERE id=%s", (id_ukolu,))
    stav = cursor.fetchone()[0]
    
    assert stav == "Probíhá"
```

---

## Spouštění testů

### Základní příkazy

**Spustit všechny testy:**
```bash
pytest
```

**Spustit testy v konkrétním souboru:**
```bash
pytest tests/test_task_manager.py
```

**Spustit konkrétní test:**
```bash
pytest tests/test_task_manager.py::test_pridani_ukolu_positivni
```

**Spustit testy s podrobným výstupem:**
```bash
pytest -v
# nebo
pytest --verbose
```

**Spustit testy s velmi podrobným výstupem:**
```bash
pytest -vv
```

**Zobrazit printy v testech:**
```bash
pytest -s
```

**Zobrazit pouze selhané testy:**
```bash
pytest --tb=short
```

### Výstup z testů

**Když testy projdou:**
```
tests/test_task_manager.py::test_pridani_ukolu_positivni PASSED
tests/test_task_manager.py::test_aktualizace_ukolu_positivni PASSED

========= 2 passed in 0.15s =========
```

**Když test selže:**
```
tests/test_task_manager.py::test_pridani_ukolu_positivni FAILED

========= FAILURES =========
test_pridani_ukolu_positivni ... 

AssertionError: assert 0 == 1
```

---

## Logování kroků v testech

### Proč logovat kroky?

Když test selže, často potřebujete vědět, **co se přesně stalo** v každém kroku. Logování vám pomůže:

✅ **Vidět každý krok** - Co se děje v testu krok za krokem  
✅ **Debugovat problémy** - Když test selže, uvidíte, kde přesně  
✅ **Dokumentovat test** - Logy ukazují, jak test funguje  
✅ **Sledovat průběh** - Vidíte, jak daleko test došel před selháním  

### Metoda 1: Použití `print()` (nejjednodušší)

**Nejjednodušší způsob** pro začátečníky je použít `print()`:

```python
def test_pridani_ukolu_s_print(db_connection):
    """Test s jednoduchým print() logováním"""
    conn, cursor = db_connection
    
    print("\n🔵 KROK 1: Přidávám úkol...")
    pridat_ukol_db(cursor, conn, "Test úkol", "Popis úkolu")
    print("✅ Úkol byl přidán")
    
    print("\n🔵 KROK 2: Kontroluji, jestli se úkol přidal...")
    cursor.execute("SELECT COUNT(*) FROM ukoly WHERE nazev='Test úkol'")
    pocet = cursor.fetchone()[0]
    print(f"📊 Počet úkolů: {pocet}")
    
    print("\n🔵 KROK 3: Assert - očekávám počet = 1")
    assert pocet == 1
    print("✅ Test prošel!")
```

**Spuštění:**
```bash
pytest tests/test_task_manager.py::test_pridani_ukolu_s_print -s
```

**Výstup:**
```
🔵 KROK 1: Přidávám úkol...
✅ Úkol byl přidán

🔵 KROK 2: Kontroluji, jestli se úkol přidal...
📊 Počet úkolů: 1

🔵 KROK 3: Assert - očekávám počet = 1
✅ Test prošel!
```

**Poznámka:** `-s` znamená "show output" - zobrazí všechny printy.

### Metoda 2: Použití Python `logging` modulu (doporučeno)

**Lepší způsob** je použít Python `logging` modul, který je profesionálnější:

```python
import logging

# Nastavení logování
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_pridani_ukolu_s_logging(db_connection):
    """Test s logging modulem"""
    logger.info("=" * 60)
    logger.info("🧪 ZAČÁTEK TESTU: test_pridani_ukolu_s_logging")
    logger.info("=" * 60)
    
    conn, cursor = db_connection
    logger.info("✅ Databázové připojení bylo získáno")
    
    logger.info("\n📝 KROK A: Přidání úkolu")
    pridat_ukol_db(cursor, conn, "Test úkol", "Popis úkolu")
    
    logger.info("\n📝 KROK B: Kontrola počtu úkolů")
    cursor.execute("SELECT COUNT(*) FROM ukoly WHERE nazev='Test úkol'")
    pocet = cursor.fetchone()[0]
    logger.info(f"📊 Počet úkolů: {pocet}")
    
    logger.info(f"\n✅ Assert - očekáváme {pocet} == 1")
    assert pocet == 1
    logger.info("✅ TEST ÚSPĚŠNĚ DOKONČEN!")
```

**Spuštění:**
```bash
# Metoda A: S -s flagem
pytest tests/test_task_manager.py::test_pridani_ukolu_s_logging -s

# Metoda B: S log-cli-level (lepší pro logging)
pytest tests/test_task_manager.py::test_pridani_ukolu_s_logging -v --log-cli-level=INFO
```

### Metoda 3: Logování v pomocných funkcích

Můžete také logovat přímo v funkcích, které testujete:

```python
import logging

logger = logging.getLogger(__name__)

def pridat_ukol_db(cursor, conn, nazev, popis):
    """Přidá úkol s logováním každého kroku"""
    logger.info(f"🔵 KROK 1: Začátek přidávání úkolu - název: '{nazev}'")
    
    if not nazev.strip():
        logger.error("❌ Chyba: Název úkolu je prázdný")
        raise ValueError("Název úkolu nesmí být prázdný")
    
    logger.info("✅ KROK 2: Validace proběhla úspěšně")
    
    datum = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logger.info(f"📅 KROK 3: Vytvoření data: {datum}")
    
    sql = "INSERT INTO ukoly (nazev, popis, stav, datum_vytvoreni) VALUES (%s, %s, %s, %s)"
    logger.info(f"💾 KROK 4: Příprava SQL dotazu")
    
    cursor.execute(sql, (nazev, popis, 'Nezahájeno', datum))
    logger.info("💾 KROK 5: SQL dotaz proveden")
    
    conn.commit()
    logger.info("✅ KROK 6: Změny uloženy (commit)")
    logger.info(f"✅ Úkol '{nazev}' byl úspěšně přidán!")
```

### Praktický příklad: Kompletní test s logováním

V projektu máte připravený soubor `tests/test_task_manager_s_logovanim.py`, který obsahuje kompletní příklady testů s detailním logováním.

**Spuštění příkladu:**
```bash
# Spustit jeden test s logováním
pytest tests/test_task_manager_s_logovanim.py::test_pridani_ukolu_positivni_s_logovanim -v --log-cli-level=INFO

# Spustit všechny testy s logováním
pytest tests/test_task_manager_s_logovanim.py -v --log-cli-level=INFO
```

**Výstup bude vypadat takto:**
```
INFO:__main__:============================================================
INFO:__main__:🧪 ZAČÁTEK TESTU: test_pridani_ukolu_positivni_s_logovanim
INFO:__main__:============================================================
INFO:__main__:✅ Databázové připojení bylo získáno z fixture
INFO:__main__:
INFO:__main__:📝 KROK A: Přidání úkolu do databáze
INFO:__main__:🔵 KROK 1: Začátek přidávání úkolu - název: 'Test úkol', popis: 'Popis úkolu'
INFO:__main__:✅ KROK 2: Validace vstupů proběhla úspěšně
INFO:__main__:📅 KROK 3: Vytvoření data: 2024-01-15 10:30:45
INFO:__main__:💾 KROK 4: Příprava SQL dotazu: INSERT INTO ukoly ...
INFO:__main__:💾 KROK 5: SQL dotaz byl proveden
INFO:__main__:✅ KROK 6: Změny byly uloženy do databáze (commit)
INFO:__main__:✅ Úkol 'Test úkol' byl úspěšně přidán!
...
```

### Užitečné emoji pro logování

Můžete použít emoji pro lepší čitelnost:

- 🔵 **Modrá koule** - Začátek kroku
- ✅ **Zelený check** - Úspěšný krok
- ❌ **Červený křížek** - Chyba
- 📝 **Poznámka** - Důležitá informace
- 💾 **Disketa** - Databázová operace
- 📊 **Graf** - Výsledek/výpočet
- 🧪 **Zkumavka** - Test
- ⚠️ **Varování** - Varovná zpráva

### Tipy pro efektivní logování

1. **Logujte začátek a konec testu**
   ```python
   logger.info("=" * 60)
   logger.info("🧪 ZAČÁTEK TESTU: test_nazev")
   logger.info("=" * 60)
   ```

2. **Logujte důležité hodnoty**
   ```python
   logger.info(f"📊 Počet úkolů: {pocet}")
   logger.info(f"📊 ID úkolu: {id_ukolu}")
   ```

3. **Logujte před assertem**
   ```python
   logger.info(f"✅ Assert - očekáváme {pocet} == 1, skutečnost = {pocet}")
   assert pocet == 1
   ```

4. **Logujte chyby**
   ```python
   logger.error(f"❌ Chyba: {chyba}")
   ```

### Shrnutí - Příkazy pro logování

| Příkaz | Popis |
|--------|-------|
| `pytest -s` | Zobrazí všechny printy |
| `pytest --log-cli-level=INFO` | Zobrazí všechny INFO logy |
| `pytest -v -s` | Podrobný výstup + printy |
| `pytest -v --log-cli-level=INFO` | Podrobný výstup + logy |

---

## Časté chyby a jejich řešení

### Chyba 1: "ModuleNotFoundError: No module named 'pytest'"

**Problém:** Pytest není nainstalovaný.

**Řešení:**
```bash
pip install pytest
```

### Chyba 2: "NameError: name 'db_connection' is not defined"

**Problém:** Test používá fixture `db_connection`, ale není správně importována.

**Řešení:** Ujistěte se, že:
1. Fixture je v `tests/conftest.py`
2. Soubor `tests/conftest.py` existuje
3. Test má `db_connection` jako parametr: `def test_nazev(db_connection):`

### Chyba 3: "AssertionError: assert 0 == 1"

**Problém:** Test očekává hodnotu 1, ale dostal 0.

**Řešení:** 
- Zkontrolujte, jestli se úkol skutečně přidal do databáze
- Zkontrolujte SQL dotaz
- Přidejte `print()` pro debugování:
```python
cursor.execute("SELECT COUNT(*) FROM ukoly WHERE nazev='Test úkol'")
pocet = cursor.fetchone()[0]
print(f"Počet úkolů: {pocet}")  # Pro debugování
assert pocet == 1
```

### Chyba 4: "pytest.raises() did not raise ValueError"

**Problém:** Test očekává, že kód vyhodí chybu, ale nevyhodil ji.

**Řešení:**
- Zkontrolujte, jestli funkce skutečně vyhodí chybu při špatném vstupu
- Zkontrolujte, jestli používáte správný typ chyby (`ValueError`, `TypeError`, atd.)

### Chyba 5: "OperationalError: (2003, 'Can't connect to MySQL server')"

**Problém:** Nelze se připojit k MySQL databázi.

**Řešení:**
1. Ujistěte se, že MySQL server běží
2. Zkontrolujte přihlašovací údaje v `tests/conftest.py`
3. Zkontrolujte, jestli databáze `test_task_manager_db` existuje

---

## Shrnutí - Klíčové pojmy

| Pojem | Popis |
|-------|-------|
| **Test** | Funkce, která kontroluje, jestli kód funguje správně |
| **assert** | Kontrola podmínky - pokud je True, test projde |
| **Fixture** | Funkce, která připravuje prostředí pro testy |
| **Pozitivní test** | Testuje správné chování se správnými vstupy |
| **Negativní test** | Testuje, jestli kód správně odmítne špatné vstupy |
| **pytest.raises()** | Kontroluje, jestli kód vyhodí očekávanou chybu |
| **yield** | V fixture rozděluje přípravu, test a úklid |

---

## Další kroky

Nyní, když znáte základy, můžete:

1. ✅ Vytvářet vlastní testy pro vaše funkce
2. ✅ Kombinovat pozitivní a negativní testy
3. ✅ Používat fixtures pro přípravu dat
4. ✅ Testovat databázové operace
5. ✅ Spouštět testy a interpretovat výsledky

**Tip:** Začněte jednoduchými testy a postupně přidávejte složitější. Praxe je klíčová!

---

## Užitečné odkazy

- [Oficiální dokumentace pytest](https://docs.pytest.org/)
- [Python assert statement](https://docs.python.org/3/reference/simple_stmts.html#assert)
- [pytest fixtures](https://docs.pytest.org/en/stable/fixture.html)

---

**Šťastné testování! 🎉**

