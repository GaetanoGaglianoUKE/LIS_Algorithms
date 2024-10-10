import csv

file_path = r"C:\Users\gaeta\Documents\Uni&Lavoro\Studio\Tesi\Datasets\New\V2_output4o_cleaned.txt"
output_dir = r"C:\Users\gaeta\Documents\Uni&Lavoro\Studio\Tesi\Datasets\New\Split2\4o"

# Lettura del file originale e separazione dei dati in x e y
x = []
y = []

with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        if "||||" in line:
            parts = line.split("||||")
            if len(parts) == 2:  # Assicurarsi che ci siano esattamente due parti
                x.append(parts[0].strip())
                y.append(parts[1].strip())

# Verifica che x e y abbiano la stessa lunghezza
assert len(x) == len(y), "Le liste x e y devono avere la stessa lunghezza!"

# Creazione dei set di training (75%), validazione (12.5%) e test (12.5%)
x_train = []
y_train = []
x_val = []
y_val = []
x_test = []
y_test = []

for i in range(len(x)):
    if i % 100 < 75:  # 75% dei dati nel training set
        x_train.append(x[i])
        y_train.append(y[i])
    elif 75 <= i % 100 < 88:  # 12.5% dei dati nel validation set
        x_val.append(x[i])
        y_val.append(y[i])
    else:  # 12.5% dei dati nel test set
        x_test.append(x[i])
        y_test.append(y[i])

# Funzione per salvare i set nei file .csv con virgolette
def salva_set(nome_file, x_set, y_set):
    with open(nome_file, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerow(["input", "output"])  # Intestazione del file con "input" e "output"
        for i in range(len(x_set)):
            writer.writerow([x_set[i], y_set[i]])  # Scrive ogni riga con virgolette

# Salva i set di training, validazione e test nei file .csv con i rispettivi nomi
salva_set(output_dir + r"\4o3_training_set.csv", x_train, y_train)
salva_set(output_dir + r"\4o3_validation_set.csv", x_val, y_val)
salva_set(output_dir + r"\4o3_test_set.csv", x_test, y_test)

print("I set sono stati salvati correttamente nei file CSV con virgolette e intestazione.")
