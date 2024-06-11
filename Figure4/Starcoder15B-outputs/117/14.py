def select_words(s, n):
    
    words = s.split()
    return [word for word in words if len([letter for letter in word if letter.lower() not in "aeiou"]) == n]


