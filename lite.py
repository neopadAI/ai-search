import ai_search.main as ai
import ai_search.learn as ht
import os

def create_file(file_name, content):
    # Create the path for the "books" folder inside another folder
    folder_path = os.path.join("books")
    
    # Ensure the folder exists, otherwise create it
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    # Create the complete path for the new file
    file_path = os.path.join(folder_path, f"{file_name}.txt")
    
    # Create the file in the specified folder
    with open(file_path, 'w') as file:
        file.write(content)

code = []
name = input('lite.name = ')
while(True):
    value = input('')
    if(value == 'exit'):
        break
    elif(value == name + '.execute'):
        print('= ', code)
    elif(value == name + '.clear'):
        code.clear()
        print('= ', code)
    elif(value == name + '.name'):
        name = input('= ')
    elif(value == name + '.array'):
        array = input('= ')
        print('=', code[int(array)])
    elif(value == name + '.array(search)'):
        value = input('= ')
        print('=', code.index(value))
    elif(value == name + '.search()'):
        ai.req = input('= ')
        ai.run()
        results = ai.result
        for result in results:
            print('= ' + result)
    elif(value == name + '.search(web)'):
        value = input('= ')
        ht.save_website_text(value)
    elif(value == name + '.create()'):
        value_name = input('.name = ')
        value_content = input('.content = ')
        create_file(value_name, value_content)
    else:
        if value == '':
            pass
        else:
            code.append(value)
