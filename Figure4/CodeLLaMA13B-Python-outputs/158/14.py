def find_max(words):
    
    if not words:
        return None
    max_word = words[0]
    max_word_count = 0
    for word in words:
        if len(word) > max_word_count:
            max_word = word
            max_word_count = len(word)
    return max_word


