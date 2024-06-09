
import re

def get_non_similar_keywords(keywords):
    non_similar_keywords = set()
    for keyword in keywords:
        normalized_keyword = re.sub(r'[- ]', '', keyword.lower())
        if normalized_keyword not in non_similar_keywords:
            non_similar_keywords.add(normalized_keyword)
    return len(non_similar_keywords)

