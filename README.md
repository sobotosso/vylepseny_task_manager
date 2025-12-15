# Vylepšený Správce Úkolů

Aplikace pro správu úkolů s MySQL databázovým backendem. Umožňuje uživatelům vytvářet, zobrazovat, aktualizovat a mazat úkoly prostřednictvím jednoduchého textového rozhraní.

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
- spuštění skriptu:
```bash
python3 script.py
```
