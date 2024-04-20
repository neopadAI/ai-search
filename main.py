import ai_search._2_0.main as ai

ai.req = input('ai-search: ')
ai.run()
results = ai.result

print('results: ')
for result in results:
    print(result)
    print()
