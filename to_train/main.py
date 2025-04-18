import os

def create_folder_if_not_exists(main_folder, folder_name):
    """
    Create a folder with the specified name inside the main folder,
    if it does not already exist.
    
    Args:
    - main_folder (str): The path of the main folder.
    - folder_name (str): The name of the folder to create.
    
    Returns:
    - str: The full path of the created folder.
    """
    folder_path = os.path.join(main_folder, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path

def unique_file_name(folder):
    """
    Generate a unique file name within the specified folder.
    
    Args:
    - folder (str): The path of the folder.
    
    Returns:
    - str: The full path of the unique file.
    """
    i = 1
    while True:
        file_name = f"{i}.html"
        file_path = os.path.join(folder, file_name)
        if not os.path.exists(file_path):
            return file_path
        i += 1

def save_text_to_file(file_path, text):
    """
    Save the provided text to a specified file.
    
    Args:
    - file_path (str): The path of the file.
    - text (str): The text to write into the file.
    """
    with open(file_path, "w") as file:
        file.write(text)

