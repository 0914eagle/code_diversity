def select_words(s, n):
    
    # your code here
    return [word for word in s.split() if len([c for c in word if c.lower() not in 'aeiou']) == n]


