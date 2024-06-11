def find_max(words):
    
    if not words:
        return ""
    max_word = words[0]
    max_chars = 0
    for word in words:
        if len(set(word)) > max_chars:
            max_word = word
            max_chars = len(set(word))
    return max_word


