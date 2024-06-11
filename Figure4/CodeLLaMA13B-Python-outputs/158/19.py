def find_max(words):
    
    # Your code here
    max_word = ""
    max_char = 0
    for word in words:
        if len(word) > max_char:
            max_char = len(word)
            max_word = word
        elif len(word) == max_char:
            if word < max_word:
                max_word = word
    return max_word


print(find_max(["name", "of", "string"]))
print(find_max(["name", "enam", "game"]))
print(find_max(["aaaaaaa", "bb", "cc"]))
