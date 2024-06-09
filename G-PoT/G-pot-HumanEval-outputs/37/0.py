
def get_closest_vowel(word: str) -> str:
    vowels = set('aeiouAEIOU')
    consonants = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
    
    found_vowel = ''
    found_consonant = False
    
    for char in reversed(word[1:-1]):
        if char in vowels:
            if found_consonant:
                return char
        elif char in consonants:
            found_consonant = True
    
    return ''
