def select_words(s, n):
    
    # Your code here
    if len(s) == 0:
        return []
    else:
        s = s.split()
        result = []
        for i in s:
            if i.isalpha() and len(i) == n:
                result.append(i)
        return result

