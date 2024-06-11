def find_max(words):
    
    # Your code here
    return max(set(words), key=words.count)


