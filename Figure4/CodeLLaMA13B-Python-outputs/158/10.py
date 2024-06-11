def find_max(words):
    
    if not words:
        return ""

    max_word = words[0]
    max_characters = 0

    for word in words:
        if len(set(word)) > max_characters:
            max_word = word
            max_characters = len(set(word))

    return max_word


