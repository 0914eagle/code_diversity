def select_words(s, n):
    
    words = s.split()
    return [word for word in words if len(word) - len(word.strip(VOWELS)) == n]

