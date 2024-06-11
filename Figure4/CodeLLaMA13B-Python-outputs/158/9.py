def find_max(words):
    
    if not words:
        return ""
    max_word = words[0]
    max_char = 0
    for word in words:
        if len(set(word)) > max_char:
            max_char = len(set(word))
            max_word = word
    return max_word


