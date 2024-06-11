def find_max(words):
    
    # TODO: implement this function
    max_word = ""
    max_len = 0
    for word in words:
        if len(set(word)) > max_len:
            max_len = len(set(word))
            max_word = word
    return max_word


