def find_max(words):
    
    max_word = ''
    max_unique = 0
    for word in words:
        unique = set(word)
        if len(unique) > max_unique:
            max_unique = len(unique)
            max_word = word
        elif len(unique) == max_unique and word < max_word:
            max_word = word
    return max_word


