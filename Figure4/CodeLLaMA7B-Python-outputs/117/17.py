def select_words(s, n):
    
    # return [w for w in s.split() if len(w) == n and w.isalpha()]
    return [w for w in s.split() if len(w) == n and w.isalpha() and w.lower() not in "aeiou"]


