
def get_non_similar_keywords(keywords):
    non_similar_keywords = set()
    for i in range(len(keywords)):
        for j in range(i+1, len(keywords)):
            if keywords[i].lower().replace("-", " ") == keywords[j].lower().replace("-", " "):
                continue
            non_similar_keywords.add(keywords[i])
    return len(non_similar_keywords)

