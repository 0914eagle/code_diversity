def find_max(words):
    
    if not words:
        return ""
    max_word = words[0]
    max_unique_char = len(set(max_word))
    for word in words[1:]:
        unique_char = len(set(word))
        if unique_char > max_unique_char:
            max_unique_char = unique_char
            max_word = word
        elif unique_char == max_unique_char:
            if word < max_word:
                max_word = word
    return max_word
