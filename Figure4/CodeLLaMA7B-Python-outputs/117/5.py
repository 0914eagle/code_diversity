def select_words(s, n):
    
    # s = s.split()
    # res = []
    # for word in s:
    #     if len(word) == n:
    #         res.append(word)
    # return res

    # return [word for word in s.split() if len(word) == n]

    return [word for word in s.split() if len(word) == n]


