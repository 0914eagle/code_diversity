def select_words(s, n):
    
    # s = s.split()
    # return [word for word in s if len(word) == n and word.isalpha()]
    return [word for word in s.split() if len(word) == n and word.isalpha()]


print(select_words("Mary had a little lamb", 4))
print(select_words("Mary had a little lamb", 3))
print(select_words("simple white space", 2))
print(select_words("Hello world", 4))
print(select_words("Uncle sam", 3))
