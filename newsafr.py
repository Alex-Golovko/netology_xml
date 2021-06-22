import collections
import json

def read_json(file_path, max_len_word=6, top_word=10):
    with open(file_path, encoding='utf-8') as news_file:
        news = json.load(news_file)
        description_word = []
        for item in news['rss']['channel']['items']:
            description = [word for word in item['description'].split(' ') if len(word) > max_len_word]
            description_word.extend(description)
            counter_words = collections.Counter(description_word)
        print(counter_words.most_common(top_word))