def find_max(words):
    
    # Your code here
    max_word = ""
    max_count = 0
    for word in words:
        count = len(set(word))
        if count > max_count:
            max_count = count
            max_word = word
    return max_word


print(find_max(["name", "of", "string"]))
print(find_max(["name", "enam", "game"]))
print(find_max(["aaaaaaa", "bb", "cc"]))
