def find_max(words):
    
    if not words:
        return None

    max_word = words[0]
    max_word_unique = len(set(max_word))

    for word in words:
        word_unique = len(set(word))
        if word_unique > max_word_unique:
            max_word = word
            max_word_unique = word_unique
        elif word_unique == max_word_unique and word < max_word:
            max_word = word

    return max_word


