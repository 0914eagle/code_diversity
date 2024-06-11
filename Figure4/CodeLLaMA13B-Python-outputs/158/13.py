def find_max(words):
    
    if not words:
        return ""
    max_word = ""
    max_count = 0
    for word in words:
        if len(word) > max_count:
            max_word = word
            max_count = len(word)
    return max_word


