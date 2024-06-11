def select_words(s, n):
    
    # Write your code here
    words = []
    for i in range(len(s)):
        if s[i].isalpha():
            if len(s[i:]) == n:
                words.append(s[i:])
    return words

# Test cases
print(select_words("Mary had a little lamb", 4))
print(select_words("Mary had a little lamb", 3))
print(select_words("simple white