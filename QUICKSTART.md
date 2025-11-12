# Rychlý start - Vylepšený Správce Úkolů

## 🚀 Rychlý návod

### 1. Aktivace virtuálního prostředí

```bash
# Přejděte do složky projektu
cd Projektove_ukoly/vylepseny_task_manager

# Aktivujte venv (macOS/Linux)
source venv/bin/activate

# Aktivujte venv (Windows)
venv\Scripts\activate
```

Po aktivaci uvidíte `(venv)` na začátku příkazové řádky.

### 2. Instalace závislostí

```bash
pip install -r requirements.txt
```

### 3. Spuštění aplikace

```bash
python script.py
```

### 4. Spuštění testů

```bash
pytest -v
```

## ⚠️ Před spuštěním zkontrolujte:

- ✅ MySQL Server je spuštěný
- ✅ Přihlašovací údaje v `src/db.py` jsou správné
- ✅ Pro testy jsou správné údaje v `tests/conftest.py`

## 📝 Poznámky

- Testy používají samostatnou testovací databázi: `test_task_manager_db`
- Aplikace používá produkční databázi: `task_manager_db`
- Po dokončení práce můžete deaktivovat venv: `deactivate`


