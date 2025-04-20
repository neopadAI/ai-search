import os
import ai_search.learn as learn
import difflib
import no_search.main as no

result = []
req = ''
books_path = "books"

def run():
    if os.path.exists(books_path) and os.path.isdir(books_path):
        books_folders = sorted([folder for folder in os.listdir(books_path) if os.path.isdir(os.path.join(books_path, folder))])
        
        if books_folders:
            for folder in books_folders:
                #print(folder)
                pass
        else:
            print("No results found")
    else:
        print("No results found")

    folders_to_open = req.lower().split()

    printed_file_content = {}

    # Iterate through the entered folder names
    for folder_name in folders_to_open:
        folder_name = folder_name.strip()  # Remove extra white spaces
        if folder_name not in no.search:
            matches = difflib.get_close_matches(folder_name, books_folders, n=len(books_folders), cutoff=0.5)

            if matches:
                for match in matches:        

                    folder_path = os.path.join(books_path, match)
                    if os.path.exists(folder_path) and os.path.isdir(folder_path):
                        file_list = sorted([f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))])

                        if file_list:
                            for file_name in file_list:
                                file_path = os.path.join(folder_path, file_name)
                                
                                with open(file_path, 'r') as file:
                                    file_content = file.read()
                                
                                if file_content not in printed_file_content.values():
                                    result.append(file_content)
                                    printed_file_content[file_name] = file_content
                        else:
                            print('Page not found')
                    else:
                        print('Page not found')
            else:
                if 'https://www.' in folder_name:
                    learn.save_website_text(folder_name)
                else:
                    pass

                if 'http://www.' in folder_name:
                    learn.save_website_text(folder_name)
                else:
                    pass

                if 'website' in folder_name:
                    learn.save_website_text('http://www.' + folder_name)
                else:
                    pass
