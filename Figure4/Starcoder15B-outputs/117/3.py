def select_words(s, n):
    
    # Your code here
    words = s.split()
    result = []
    for word in words:
        if len(word) == n:
            result.append(word)
    return result

