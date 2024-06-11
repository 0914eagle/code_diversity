def select_words(s, n):
    
    # s = s.split()
    # res = []
    # for i in s:
    #     if len(i) == n:
    #         res.append(i)
    # return res

    # return [i for i in s.split() if len(i) == n]

    # return [i for i in s.split() if len(i) == n]

    return [i for i in s.split() if len(i) == n]


print(select_words("Mary had a little lamb", 4))
print(select_words("Mary had a little lamb", 3))
print(select_words("simple white space", 2))
print(select_words("Hello world", 4))
print(select_words("Uncle sam", 3))
