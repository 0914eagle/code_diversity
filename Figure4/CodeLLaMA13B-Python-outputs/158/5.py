def find_max(words):
    
    if not words:
        return ""

    max_word = ""
    max_word_count = 0

    for word in words:
        if len(word) > max_word_count:
            max_word = word
            max_word_count = len(set(word))
        elif len(word) == max_word_count:
            if word < max_word:
                max_word = word

    return max_word


if __name__