def find_max(words):
    
    # Write your code here
    return max(set(words), key=words.count)


