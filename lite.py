import ai_search._2_0.main as ai
import ai_search._2_0.impare as ht
import os

def crea_file(nome_file, content):
    # Creare il percorso della cartella "books" all'interno di un'altra cartella
    percorso_cartella = os.path.join("books")
    
    # Assicurati che la cartella esista, altrimenti creala
    if not os.path.exists(percorso_cartella):
        os.makedirs(percorso_cartella)
    
    # Crea il percorso completo del nuovo file
    percorso_file = os.path.join(percorso_cartella, f"{nome_file}.txt")
    
    # Crea il file nella cartella specificata
    with open(percorso_file, 'w') as file:
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
        crea_file(value_name, value_content)
    else:
        if value == '':
            pass
        else:
            code.append(value)
