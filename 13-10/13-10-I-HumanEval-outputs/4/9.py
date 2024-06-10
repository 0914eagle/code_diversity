
from typing import Dict

def histogram(test: str) -> Dict[str, int]:
    
    # Your code here
    word_count = {}
    for word in test.split():
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1

    max_count = max(word_count.values())
    most_frequent_words = [word for word, count in word_count.items() if count == max_count]

    return {word: max_count for word in most_frequent_words}


