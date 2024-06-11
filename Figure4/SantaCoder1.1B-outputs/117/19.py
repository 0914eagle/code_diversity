def select_words(s, n):
    
    # Write your code here
    return [word for word in s.split() if len(word) == n and all(c in "bcdfghjklmnpqrstvwxyz" for c in word)]

