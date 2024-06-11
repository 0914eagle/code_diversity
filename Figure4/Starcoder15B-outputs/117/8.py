def select_words(s, n):
    
    # Your code here
    if s == "":
        return []
    else:
        s = s.split()
        result = []
        for word in s:
            if len(word) == n:
                result.append(word)
        return result

#