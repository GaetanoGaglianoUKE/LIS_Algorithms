import openai
import os
import time

# Inserisci la tua chiave API di OpenAI qui
openai.api_key = 'API_KEY'

input_folder = "C:\\Users\\gaeta\\Documents\\Uni&Lavoro\\Studio\\Tesi\\Datasets\\New\\Storie2"
output_folder = "C:\\Users\\gaeta\\Documents\\Uni&Lavoro\\Studio\\Tesi\\Datasets\\New\\Tradotte4t"

def chat_with_gpt(prompt, model="gpt-4-turbo"):
    try:
        # Richiesta all'API di OpenAI
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": """Interpreta le frasi che ti invierò come se fossi un traduttore che riesce a tradurre dalla lingua italiana alla lingua italiana dei segni, standardizzando le parole che ti vengono inviate. Ecco le indicazioni:
1. Per ogni frase ricevuta, crea una traduzione nelle parole corrispondenti, nella traduzione unisci le singole parole con " + ".
2. Nella risposta scrivi solo le parole standardizzate senza aggiungere altre informazioni.
3. Per i verbi usa l'infinito e indica tra parentesi se presente, passato o futuro nella traduzione.
4. Rispettare le convenzioni e le regole della LIS, soprattutto l'ordine Soggetto+oggetto+verbo (SOV) e la grammatica italiana.
5. Dividi il testo in input in frasi singole per semplificare i concetti.
Scrivi la traduzione in maiuscolo e fornisci come output una tabella contenente a sinistra la frase in italiano e a destra la frase in LIS."""},
                {"role": "user", "content": prompt}
            ]
        )

        # Estrarre la risposta
        message = response['choices'][0]['message']['content']
        return message

    except Exception as e:
        return f"Si è verificato un errore: {str(e)}"

def process_files(input_folder, output_folder):
    # Ordina i file per nome in modo numerico (1.txt, 2.txt, ...)
    file_list = sorted([f for f in os.listdir(input_folder) if f.endswith(".txt")], key=lambda x: int(x.split('.')[0]))

    for filename in file_list:
        input_file_path = os.path.join(input_folder, filename)
        output_file_path = os.path.join(output_folder, filename)  # Usa lo stesso nome per l'output

        try:
            with open(input_file_path, 'r', encoding='utf-8') as file:
                user_input = file.read()

            # Chiamare la funzione con il prompt dell'utente
            gpt_response = chat_with_gpt(user_input)

            # Scrivere la risposta nel file di output
            with open(output_file_path, 'w', encoding='utf-8') as file:
                file.write(gpt_response)

            print(f"Elaborato: {filename}")  # Tracking dei progressi

        except Exception as e:
            print(f"Errore con il file {filename}: {str(e)}")

if __name__ == "__main__":
    process_files(input_folder, output_folder)