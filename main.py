import ai_search.main as ai

ai.req = input('ai-search: ')
ai.run()
results = ai.result

print('results: ')
for result in results:
    print(result)
    print()
