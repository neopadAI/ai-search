import requests
from bs4 import BeautifulSoup
import os

def save_website_text(url):
    site_name = url.replace("https://www.", "").replace("http://www.", "")
    
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        
        # Use BeautifulSoup to parse the HTML content
        soup = BeautifulSoup(html_content, 'html.parser')
        
        visible_text = soup.get_text()
        
        visible_text_cleaned = '\n'.join(line.strip() for line in visible_text.splitlines() if line.strip())
        
        if not os.path.exists('books'):
            os.makedirs('books')
        
        # Create a subfolder with the website name if it doesn't already exist
        site_folder = f'books/{site_name}'
        if not os.path.exists(site_folder):
            os.makedirs(site_folder)
            
        with open(f'{site_folder}/index.txt', 'w', encoding='utf-8') as file:
            file.write(visible_text_cleaned)
                
        print(f"The text of the website {url} has been saved in '{site_folder}/index.txt'")
    else:
        print(f"Error {response.status_code} while trying to fetch data from the website {url}")
