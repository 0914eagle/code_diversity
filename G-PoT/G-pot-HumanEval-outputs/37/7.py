
def get_closest_vowel(word: str) -> str:
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    consonants = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
    
    found_vowel = ''
    found_consonant = False
    
    for char in reversed(word[1:-1]):
        if char in vowels:
            found_vowel = char
            break
        elif char in consonants:
            found_consonant = True
    
    return found_vowel if found_consonant else ''
