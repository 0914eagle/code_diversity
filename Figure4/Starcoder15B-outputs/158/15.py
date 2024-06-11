def find_max(words):
    
    # YOUR CODE HERE
    # raise NotImplementedError()
    max_len = 0
    max_word = ''
    for word in words:
        if len(set(word)) > max_len:
            max_len = len(set(word))
            max_word = word
    return max_word


