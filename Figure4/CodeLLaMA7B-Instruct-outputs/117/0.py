

def select_words(s, n):
    
    words = s.split()
    consonant_words = []
    for word in words:
        vowels = "aeiou"
        if len([c for c in word if c.lower() not in vowels]) == n:
            consonant_words.append(word)
    return consonant_words


