# Funzione per rimuovere righe vuote da un file di testo
def rimuovi_righe_vuote(file_path):
    # Leggi tutte le righe dal file
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Filtra le righe, rimuovendo quelle vuote o composte solo da spazi
    righe_non_vuote = [line for line in lines if line.strip()]

    # Sovrascrivi il file con le righe non vuote
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(righe_non_vuote)

    print(f"File aggiornato: righe vuote rimosse da {file_path}")


# Esempio di utilizzo
if __name__ == "__main__":
    file_path = 'C:/Users/gaeta/Documents/Uni&Lavoro/Studio/Tesi/Datasets/New/output4t.txt'  # Modifica con il tuo percorso
    rimuovi_righe_vuote(file_path)