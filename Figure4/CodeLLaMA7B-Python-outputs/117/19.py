def select_words(s, n):
    
    # s = s.split()
    # print(s)
    # res = []
    # for word in s:
    #     if len(word) == n:
    #         res.append(word)
    # return res

    # return [word for word in s.split() if len(word) == n]

    return [word for word in s.split() if len(word) == n]


print(select_words("Mary had a little lamb", 4))
print(select_words("Mary had a little lamb", 3))
print(select_words("simple white space", 2))
print(select_words("Hello world", 4))
print(select_words("Uncle sam", 3))
