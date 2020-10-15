import json
from collections import Counter
def get_words(filename):
  results = []
  with open(filename, encoding="utf-8") as first_json:    data = json.load(first_json)
  first_example = data["rss"]["channel"]["items"]
  for result in first_example:
    new_result = result["description"].lower().split()
    for new in new_result:
        if len(new) > 6:
            results.append(new)
 
  last_list = Counter(results)
  sorted_list =  last_list.most_common(10)
  return f'топ 10 самые часто используемые слова:{sorted_list}'
  
print(get_words("newsafr.json"))

