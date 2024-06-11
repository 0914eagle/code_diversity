def select_words(s, n):
    
    # TODO: Write your code here
    return [w for w in s.split() if len(w) == n and w.isalpha()]


