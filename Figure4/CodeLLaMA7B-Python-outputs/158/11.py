def find_max(words):
    
    if not words:
        return ""
    max_word = words[0]
    max_count = len(set(max_word))
    for word in words[1:]:
        if len(set(word)) > max_count:
            max_word = word
            max_count = len(set(word))
    return max_word
