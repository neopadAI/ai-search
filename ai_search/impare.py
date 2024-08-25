import requests
from bs4 import BeautifulSoup
import os

def save_website_text(url):
    # Remove the prefix "https://www." or "http://www." from the site name
    site_name = url.replace("https://www.", "").replace("http://www.", "").replace("https://", "").replace("http://", "")
    
    # Get the HTML content of the website
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        
        # Use BeautifulSoup to parse the HTML content
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Get the visible text from the parsed HTML
        visible_text = soup.get_text()
        
        # Remove excess whitespace from each line of text
        visible_text_cleaned = '\n'.join(line.strip() for line in visible_text.splitlines() if line.strip())
        
        # Create the 'books' directory if it does not exist
        if not os.path.exists('books'):
            os.makedirs('books')
        
        # Create a subfolder named after the site if it does not exist
        site_folder = os.path.join('books', site_name)
        if not os.path.exists(site_folder):
            os.makedirs(site_folder)
            
        # Save the cleaned text in 'index.txt' within the 'books/site_name' folder
        with open(os.path.join(site_folder, 'index.txt'), 'w', encoding='utf-8') as file:
            file.write(visible_text_cleaned)
                
        print(f"The text of the website {url} has been saved in '{os.path.join(site_folder, 'index.txt')}'")
    else:
        print(f"Error {response.status_code} while trying to fetch data from the website {url}")

# Example usage
url_site = 'https://example.com'  # Replace with the URL of the website you want to scrape
save_website_text(url_site)
