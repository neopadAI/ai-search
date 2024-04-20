import requests
from bs4 import BeautifulSoup
import os

def save_website_text(url):
    # Rimuovi il prefisso "https://" dal nome del sito
    site_name = url.replace("https://www.", "").replace("http://www.", "")
    
    # Ottieni il contenuto HTML del sito web
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        
        # Utilizza BeautifulSoup per analizzare il contenuto HTML
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Ottieni il testo visibile dall'utente
        visible_text = soup.get_text()
        
        # Rimuovi gli spazi in eccesso da ogni riga di testo
        visible_text_cleaned = '\n'.join(line.strip() for line in visible_text.splitlines() if line.strip())
        
        # Crea la cartella 'books' se non esiste già
        if not os.path.exists('books'):
            os.makedirs('books')
        
        # Crea la sottocartella con il nome del sito web se non esiste già
        site_folder = f'books/{site_name}'
        if not os.path.exists(site_folder):
            os.makedirs(site_folder)
            
        # Salva il testo pulito in un file di nome 'index.txt' nella cartella 'books' con il nome del sito web come sottocartella
        with open(f'{site_folder}/index.txt', 'w', encoding='utf-8') as file:
            file.write(visible_text_cleaned)
                
        print(f"The text of the website {url} has been saved in '{site_folder}/index.txt'")
    else:
        print(f"Error {response.status_code} while trying to fetch data from the website {url}")

# Esempio di utilizzo
url_site = ''
