def select_words(s, n):
    
    # your code here
    # return []
    return [word for word in s.split() if len([letter for letter in word if letter.lower() not in "aeiou"]) == n]

