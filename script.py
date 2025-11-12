from src.db import vytvorit_db, pripojeni_db, vytvorit_tabulku_ukoly
from src.task_manager import hlavni_menu

if __name__ == "__main__":
    vytvorit_db()
    connection = pripojeni_db()
    if connection:
        vytvorit_tabulku_ukoly(connection)
        hlavni_menu(connection)
        connection.close()
    else:
        print("Nepodařilo se připojit k databázi, program končí.")
