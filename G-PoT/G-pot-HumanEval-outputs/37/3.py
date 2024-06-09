
def get_closest_vowel(word: str) -> str:
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
    found_vowel = ''
    found_consonant = False
    
    for char in reversed(word[1:-1]):  # Exclude first and last characters
        if char in vowels:
            if found_consonant:
                found_vowel = char
                break
        elif char in consonants:
            found_consonant = True
    
    return found_vowel
