def find_max(words):
    
    if not words:
        return ""
    max_word = words[0]
    max_char = set(max_word)
    for word in words:
        if len(set(word)) > len(max_char):
            max_word = word
            max_char = set(word)
        elif len(set(word)) == len(max_char):
            if word < max_word:
                max_word = word
    return max_word


if