import pandas as pd


def load_dataset(file_path):
    """Carica il dataset come DataFrame da file .csv"""
    return pd.read_csv(file_path)


def calculate_statistics(df, text_column, delimiter=' '):
    """
    Calcola le statistiche per il numero di parole in una colonna di testo del DataFrame.

    Args:
        df (pd.DataFrame): Il DataFrame contenente il testo.
        text_column (str): La colonna da analizzare.
        delimiter (str): Il delimitatore per separare le parole (default: spazio ' ').

    Returns:
        dict: Statistiche calcolate (numero frasi, minimo, massimo, media).
    """
    # Controlla se la colonna esiste nel dataset
    if text_column not in df.columns:
        raise ValueError(f"La colonna '{text_column}' non è presente nel dataset")

    # Calcola il numero di frasi
    num_sentences = len(df)

    # Rimuovi spazi multipli e pulisci il testo per evitare errori di conteggio
    df[text_column] = df[text_column].apply(lambda x: ' '.join(str(x).split()))

    # Calcola il numero di parole per ogni frase nella colonna specificata usando il delimitatore
    df['num_words'] = df[text_column].apply(lambda x: len(str(x).split(delimiter)))

    # Calcola le statistiche sulle parole
    num_words_min = df['num_words'].min()
    num_words_max = df['num_words'].max()
    num_words_mean = df['num_words'].mean()

    return {
        'Numero di frasi': num_sentences,
        'Numero minimo di parole': num_words_min,
        'Numero massimo di parole': num_words_max,
        'Numero medio di parole': num_words_mean,
    }


def save_statistics(stats, file, dataset_file_name):
    """
    Salva le statistiche calcolate su un file di testo.

    Args:
        stats (dict): Dizionario contenente le statistiche su input e output.
        file (file object): File in cui scrivere le statistiche.
        dataset_file_name (str): Nome del file del dataset.
    """
    # Formatta il nome del dataset
    file.write(f"Statistiche per il dataset {dataset_file_name}:\n")

    # Stampa le statistiche per la colonna 'input'
    file.write("Input:\n")
    file.write(f"  Numero di frasi: {stats['input']['Numero di frasi']}\n")
    file.write(f"  Numero minimo di parole: {stats['input']['Numero minimo di parole']}\n")
    file.write(f"  Numero massimo di parole: {stats['input']['Numero massimo di parole']}\n")
    file.write(f"  Numero medio di parole: {stats['input']['Numero medio di parole']}\n")

    # Stampa le statistiche per la colonna 'output'
    file.write("Output:\n")
    file.write(f"  Numero di frasi: {stats['output']['Numero di frasi']}\n")
    file.write(f"  Numero minimo di parole: {stats['output']['Numero minimo di parole']}\n")
    file.write(f"  Numero massimo di parole: {stats['output']['Numero massimo di parole']}\n")
    file.write(f"  Numero medio di parole: {stats['output']['Numero medio di parole']}\n")
    file.write("\n")


def main(train_file, val_file, test_file, output_file):
    """
    Carica i dataset, calcola le statistiche su input e output, e le salva su un file di testo.

    Args:
        train_file (str): Percorso del file di training.
        val_file (str): Percorso del file di validazione.
        test_file (str): Percorso del file di test.
        output_file (str): Percorso del file di output.
    """
    # Carica i dataset
    train_df = load_dataset(train_file)
    val_df = load_dataset(val_file)
    test_df = load_dataset(test_file)

    # Calcola le statistiche per ciascun dataset e ciascuna colonna
    with open(output_file, 'w') as f:
        for dataset_name, df in [('4t_training_set.csv', train_df),
                                 ('4t_validation_set.csv', val_df),
                                 ('4t_test_set.csv', test_df)]:
            # Calcola le statistiche per input (utilizza lo spazio come separatore)
            input_stats = calculate_statistics(df, 'input')

            # Calcola le statistiche per output (utilizza il '+' come separatore)
            output_stats = calculate_statistics(df, 'output', delimiter='+')

            # Organizza le statistiche in un dizionario per input e output
            stats = {'input': input_stats, 'output': output_stats}

            # Salva le statistiche su un file di testo
            save_statistics(stats, f, dataset_name)


if __name__ == "__main__":
    # Percorsi dei file csv
    test_file = r'C:\Users\gaeta\Documents\PyCharm\s2s_training\data\csv\4o3_test_set.csv'  # Sostituisci con il percorso del file
    train_file = r'C:\Users\gaeta\Documents\PyCharm\s2s_training\data\csv\4o3_training_set.csv'  # Sostituisci con il percorso del file
    val_file = r'C:\Users\gaeta\Documents\PyCharm\s2s_training\data\csv\4o3_validation_set.csv'  # Sostituisci con il percorso del file
    output_file = r'C:\Users\gaeta\Downloads\Nuova cartella\(4o3)Stats.txt'  # Nome del file di output

    # Esegue il calcolo delle statistiche e salva i risultati
    main(train_file, val_file, test_file, output_file)
