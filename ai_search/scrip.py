import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, unquote

def download_file(url, folder):
    try:
        r = requests.get(url, allow_redirects=True)
        filename = os.path.basename(urlparse(url).path)
        with open(os.path.join(folder, filename), 'wb') as file:
            file.write(r.content)
        print(f"Downloaded: {url}")
    except Exception as e:
        #print(f"Failed to download: url: '{url}': error'{e}'")
        pass

def download_website(url, folder="books/"):
    print('preparation...')
    response = requests.get(url)
    if response.status_code == 200:
        # Parses the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        domain = urlparse(url).netloc
        path = urlparse(url).path
        # Creates a folder for the website
        site_folder = os.path.join(folder, domain, *path.split("/"))
        os.makedirs(site_folder, exist_ok=True)
        with open(os.path.join(site_folder, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(response.text)
        for tag in soup.find_all(['script', 'link', 'style']):
            if tag.has_attr('src'):
                src = tag['src']
                absolute_src = urljoin(url, src)
                download_file(absolute_src, site_folder)
                tag['src'] = os.path.relpath(absolute_src, site_folder)
            elif tag.name == 'link' and tag.has_attr('href'):
                href = tag['href']
                absolute_href = urljoin(url, href)
                download_file(absolute_href, site_folder)
                tag['href'] = os.path.relpath(absolute_href, site_folder)
        # Downloads images
        for img in soup.find_all('img'):
            src = img.get('src')
            if src:
                absolute_src = urljoin(url, src)
                download_file(absolute_src, site_folder)
                img['src'] = os.path.relpath(absolute_src, site_folder)
        # Downloads videos
        for video in soup.find_all('video'):
            src = video.get('src')
            if src:
                absolute_src = urljoin(url, src)
                download_file(absolute_src, site_folder)
                video['src'] = os.path.relpath(absolute_src, site_folder)
        # Finds and downloads links to internal pages and sections of the website
        for link in soup.find_all('a', href=True):
            href = unquote(link['href'])
            if urlparse(href).scheme in ("http", "https") and urlparse(href).netloc == domain:
                download_website(href, folder)
        # Saves the updated HTML code
        with open(os.path.join(site_folder, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"Website '{domain + path}' downloaded successfully.")
    else:
        print(f"Failed to download website: {response.status_code}")

def move_folders_to_books_folder(root_folder):
    books_folder = os.path.join(root_folder, "books")
    os.makedirs(books_folder, exist_ok=True)
    for root, dirs, files in os.walk(root_folder):
        for d in dirs:
            if d != "books":
                os.rename(os.path.join(root, d), os.path.join(books_folder, d))
    print("All folders moved to 'books' folder.")
