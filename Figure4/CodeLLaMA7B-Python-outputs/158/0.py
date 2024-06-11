def find_max(words):
    
    if len(words) == 0:
        return None
    max_word = words[0]
    max_count = len(set(max_word))
    for word in words[1:]:
        if len(set(word)) > max_count:
            max_count = len(set(word))
            max_word = word
    return max_word
