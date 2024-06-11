def find_max(words):
    
    if not words:
        return ""

    max_word = ""
    max_chars = 0
    for word in words:
        if len(word) > max_chars:
            max_word = word
            max_chars = len(set(word))
        elif len(word) == max_chars:
            if word < max_word:
                max_word = word
    return max_word


if __name__ == "__main__":