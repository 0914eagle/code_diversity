
def remove_duplicates(text):
    words = text.lower().split()
    unique_words = set()
    result = []
    for word in words:
        if word not in unique_words:
            unique_words.add(word)
            result.append(word)
        else:
            result.append(".")
    return " ".join(result)

