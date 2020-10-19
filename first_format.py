import json
from collections import Counter


def get_words(filename: str, top_size: int, min_word_len: int) -> str:
    all_words = []

    with open(filename, encoding="utf-8") as first_json:
        data = json.load(first_json)
        news = data["rss"]["channel"]["items"]

    for article in news:
        words = article["description"].lower().split()
        for word in words:
            if len(word) > min_word_len:
                all_words.append(word)

    counter = Counter(all_words)
    top_list = counter.most_common(top_size)
    return f"топ {top_size} самые часто используемые слова:{top_list}"

print(get_words("newsafr.json", top_size=10, min_word_len=6))
