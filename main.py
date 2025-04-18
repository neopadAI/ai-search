# to-train
import to_train.main as train

main_folder = "books"

category_name = input("Category: ")
category_folder_path = train.create_folder_if_not_exists(main_folder, category_name)

text = input("Content: ")
html_file_path = train.unique_file_name(category_folder_path)

train.save_text_to_file(html_file_path, text)


# request
import ai_search.main as ai

ai.req = input('ai-search: ')
ai.run()
results = ai.result

print('results: ')
for result in results:
    print(result)
    print()
