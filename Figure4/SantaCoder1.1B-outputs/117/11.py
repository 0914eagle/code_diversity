def select_words(s, n):
    
    # Write your code here
    return [w for w in s.split() if len(w) == n and w[0].isalpha()]

