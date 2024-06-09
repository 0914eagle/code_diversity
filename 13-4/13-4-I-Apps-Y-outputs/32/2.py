
import re

def get_non_similar_keywords(keywords):
    non_similar_keywords = set()
    for keyword in keywords:
        keyword = re.sub(r'-', ' ', keyword).lower()
        if keyword not in non_similar_keywords:
            non_similar_keywords.add(keyword)
    return len(non_similar_keywords)

