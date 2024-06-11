def select_words(s, n):
    
    # s = s.split()
    # return [word for word in s if len(word) == n and word.isalpha()]
    return [word for word in s.split() if len(word) == n and word.isalpha()]


