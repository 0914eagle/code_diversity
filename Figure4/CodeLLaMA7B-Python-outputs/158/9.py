def find_max(words):
    
    if not words:
        return ""

    max_word = words[0]
    max_unique_chars = len(set(max_word))

    for word in words[1:]:
        unique_chars = len(set(word))
        if unique_chars > max_unique_chars:
            max_word = word
            max_unique_chars = unique_chars
        elif unique_chars == max_unique_chars:
            if word < max_word:
                max_word = word

    return max_word
