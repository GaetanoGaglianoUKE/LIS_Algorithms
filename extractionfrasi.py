import os


# Funzione per estrarre frasi in italiano e LIS dai file con pulizia di caratteri indesiderati
def estrai_frasi(file_path):
    frasi = []
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read().strip()  # Leggi tutto il contenuto e rimuovi spazi vuoti
        # Dividi il contenuto in righe
        lines = content.split('\n')

        for line in lines:
            # Rimuovi spazi extra e caratteri speciali all'inizio/fine
            line = line.strip()
            if line:  # Controlla che la riga non sia vuota
                parts = line.split('|')
                if len(parts) >= 3:
                    frase_italiano = parts[1].strip()  # Pulisci eventuali spazi vuoti
                    frase_lis = parts[2].strip()  # Pulisci eventuali spazi vuoti
                    # Concatena le frasi con il separatore "||||"
                    frasi.append(f'{frase_italiano}||||{frase_lis}')
    return frasi


# Funzione per creare un file di output
def crea_file_output(output_path, frasi):
    with open(output_path, 'w', encoding='utf-8') as f:
        for frase in frasi:
            # Scrivi ogni coppia di frasi su una nuova riga
            f.write(frase + '\n')


# Funzione principale per elaborare i file nella directory di input
def processa_directory(input_dir, output_file):
    tutte_le_frasi = []

    # Scansiona tutti i file nella directory di input
    for filename in os.listdir(input_dir):
        file_path = os.path.join(input_dir, filename)
        if os.path.isfile(file_path):
            tutte_le_frasi.extend(estrai_frasi(file_path))

    # Crea il file di output
    crea_file_output(output_file, tutte_le_frasi)


if __name__ == "__main__":
    # Directory di input e file di output
    input_dir = 'C:/Users/gaeta/Documents/Uni&Lavoro/Studio/Tesi/Datasets/New/Tradotte4t'  # Modifica con la tua directory
    output_file = 'C:/Users/gaeta/Documents/Uni&Lavoro/Studio/Tesi/Datasets/New/output4t.txt'  # Modifica con il percorso del file di output

    # Esegui il processo
    processa_directory(input_dir, output_file)

    print(f"File di output creato: {output_file}")