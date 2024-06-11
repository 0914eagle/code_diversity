def select_words(s, n):
    
    # Your code here
    return [w for w in s.split() if len(w) == n and all(c in "bcdfghjklmnpqrstvwxyz" for c in w)]


