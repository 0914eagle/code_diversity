def find_max(words):
    
    # Your code here
    return max(set(words), key=words.count)


print(find_max(["name", "of", "string"]))
print(find_max(["name", "enam", "game"]))
print(find_max(["aaaaaaa", "bb" ,"cc"]))
