
def get_non_similar_keywords(keywords):
    non_similar_keywords = set()
    for i in range(len(keywords)):
        keyword1 = keywords[i].replace("-", " ").lower()
        for j in range(i+1, len(keywords)):
            keyword2 = keywords[j].replace("-", " ").lower()
            if keyword1 == keyword2:
                non_similar_keywords.add(keyword1)
    return len(non_similar_keywords)

