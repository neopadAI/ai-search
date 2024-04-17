import os
import difflib

# Percorso della cartella "books"
books_path = "books"

# Verifica se la cartella "books" esiste
if os.path.exists(books_path) and os.path.isdir(books_path):
    # Lista delle cartelle nella cartella "books"
    cartelle_books = sorted([cartella for cartella in os.listdir(books_path) if os.path.isdir(os.path.join(books_path, cartella))])
    
    if cartelle_books:
        for cartella in cartelle_books:
            print(cartella)
    else:
        print("risultati non trovati")
else:
    print("risultati non trovati")

# Chiedi all'utente di inserire i nomi delle cartelle (separati da virgole)
cartelle_da_aprire = input("ai-search: ").split(' ')

# Dizionario per tenere traccia del contenuto dei file già stampati
file_content_stampati = {}

# Ciclo attraverso i nomi delle cartelle inseriti
for folder_name in cartelle_da_aprire:
    folder_name = folder_name.strip()  # Rimuovi spazi bianchi extra
    
    # Trova le cartelle più simili
    matches = difflib.get_close_matches(folder_name, cartelle_books, n=len(cartelle_books), cutoff=0.5)

    # Verifica se sono stati trovati corrispondenze
    if matches:
        for match in matches:        

            # Verifica se la cartella esiste all'interno della cartella "books"
            folder_path = os.path.join(books_path, match)
            if os.path.exists(folder_path) and os.path.isdir(folder_path):
                # Lista dei file nella cartella specificata
                file_list = sorted([f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))])

                if file_list:
                    for file_name in file_list:
                        file_path = os.path.join(folder_path, file_name)
                        
                        # Leggi il contenuto del file
                        with open(file_path, 'r') as file:
                            file_content = file.read()
                        
                        # Verifica se il contenuto del file è già stato stampato
                        if file_content not in file_content_stampati.values():
                            print(file_content)
                            print()
                            
                            # Aggiorna il dizionario dei contenuti dei file stampati
                            file_content_stampati[file_name] = file_content
                else:
                    print('nessun post trovato')
            else:
                print('pagina non trovata')
    else:
        print(f"pagina non trovata")
