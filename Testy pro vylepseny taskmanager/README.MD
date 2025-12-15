# Detailní popis testů Vylepšený task manager

## Úvod k testům
Testovací skript pokrývá hlavní funkce CRUD (Create, Read, Update, Delete) pro správu úkolů v databázi MySQL. Testy jsou navrženy tak, aby ověřovaly jak správné fungování funkcí při platných vstupních datech (pozitivní scénáře), tak i správnou reakci aplikace na špatné a neplatné vstupy (negativní scénáře).

POZOR: testy jsou jako vnořená složka ve vylepšeném TASK MANAGERU, ideálně si je vytáhnout mimo

---

## Detailní popis testu

- **Testy pracují s testovací databází: test_task_manager_db. Pokud DB neexistuje, před spuštěním testů je vytvoena, před spuštěním každého testu se vyčistí, aby všechny testy byly nezávislé a neovlivňovaly se navzájem.
- Každý test používá `fixture` (`db_connection`), která vytvoří připojení k DB, tabulku úkolů (pokud neexistuje) a před spuštěním testu tabulku vyčistí.
- Po testu tabulka opět projde vyčištěním (pokud není úklid zakomentovaný).
- Testy volají přímo funkce, které implementují operace nad databází (přidání úkolu, aktualizace stavu, odstranění úkolu).
- Každý test ověřuje výsledky pomocí asert (kontrola počtu záznamů, hodnot v databázi nebo očekávaných výjimek).
- V negativních testech se očekávají výjimky, pokud jsou vstupy neplatné nebo chybné.

---

## Detailní popis jednotlivých testovacích scénářů

### 1. test_pridani_ukolu_pozitivni
- **Co testuje:** Přidání nového úkolu s platným názvem a popisem.
- **Postup:** Funkce vloží do DB úkol "Test úkol" s popisem "Popis úkolu" a ověří, zda se úkol skutečně uloží (kontrola existence 1 záznamu).
- **Cíl:** Potvrzení, že přidání úkolu funguje správně.
  
### 2. test_pridani_ukolu_negativni
- **Co testuje:** Chování při přidání úkolu s prázdným názvem.
- **Postup:** Pokusí se přidat úkol s prázdným názvem (""), očekává upozornění na chybu `ValueError`.
- **Cíl:** Ověřit validaci názvu úkolu a správnou reakci na neplatný vstup.

### 3. test_pridani_ukolu_negativni_popis
- **Co testuje:** Chování při přidání úkolu s prázdným popisem.
- **Postup:** Pokusí se přidat úkol s platným názvem, ale prázdným popisem, očekává upozornění na chybu `ValueError`.
- **Cíl:** Ověřit validaci popisu při přidávání úkolu.

### 4. test_aktualizace_ukolu_positivni
- **Co testuje:** Aktualizaci stavu úkolu na platnou hodnotu.
- **Postup:** Nejprve přidá úkol s názvem "Úkol k aktualizaci", vyhledá jeho ID, následně aktualizuje stav na "Hotovo" a ověří správnost aktualizace.
- **Cíl:** Potvrdit, že aktualizace stavu úkolu funguje správně.

### 5. test_aktualizace_ukolu_negativni
- **Co testuje:** Reakci na neplatný stav při aktualizaci úkolu.
- **Postup:** Přidá úkol "Úkol nevalidní stav", vyhledá ID, pokusí se nastavit neplatný stav (např. "Neplatný stav") a očekává `ValueError`.
- **Cíl:** Ověřit, že je správně ošetřeno neplatné zadání stavu.

### 6. test_odstraneni_ukolu_positivni
- **Co testuje:** Správné odstranění existujícího úkolu.
- **Postup:** Přidá úkol "Úkol k odstranění", vyhledá ID, smaže ho, ověří, že úkol už v databázi není.
- **Cíl:** Potvrdit, že odstranění úkolu funguje správně.

### 7. test_odstraneni_ukolu_negativni
- **Co testuje:** Chování při pokusu odstranit neexistující úkol.
- **Postup:** Pokusí se odstranit úkol s nesmyslným ID (999999) a očekává, že to úkol nebude odstraněn (tabulka zůstává stejná).
- **Cíl:** Ověřit, že odstranění neexistujícího záznamu nevyvolá chybu a nemění data.

## Spuštění testu (pro macos prostředí)
- vytvoříme virtuální prostředí: 
```bash
python -m venv venv
```
- aktivujeme virtuální prostředí: 
```bash
source venv/bin/activate
```
- nainstalujeme závislosti: 
```bash
pip install -r requirements.txt
```
- před spuštěním testů je nutné nastavit přihlašovací údaje pro připojení k DB:
```bash
DB_CONFIG = {
    "host": "localhost",
    "user": "user",
    "password": "heslo",
    "database": "test_task_manager_db"
}
```
- spustíme testy: 
```bash
pytest tests.py
```
Všechny výsledky bychom měli vidět následovně:
```bash
tests.py::test_pridani_ukolu_positivni PASSED                                                                                                        [ 14%]
tests.py::test_pridani_ukolu_negativni PASSED                                                                                                        [ 28%]
tests.py::test_pridani_ukolu_negativni_popis PASSED                                                                                                  [ 42%]
tests.py::test_aktualizace_ukolu_positivni PASSED                                                                                                    [ 57%]
tests.py::test_aktualizace_ukolu_negativni PASSED                                                                                                    [ 71%]
tests.py::test_odstraneni_ukolu_positivni PASSED                                                                                                     [ 85%]
tests.py::test_odstraneni_ukolu_negativni PASSED                                                                                                     [100%]
```
---

## Shrnutí
- Testy slouží k ověření základního i hraničního chování vašich CRUD funkcí.
- Každý test simuluje konzistentní scénář reálného použití nebo chybové situace.
- Validace vstupů je ošetřena v aplikaci i v testech.
- Čistota databáze mezi testy zajišťuje nezávislost testů bez vzájemného ovlivnění.
- Popisy úkolů v testech jsou pouze orientační štítky pro lepší srozumitelnost kódu a nemají váhu mimo testovací prostředí.

