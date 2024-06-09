
def get_closest_vowel(word: str) -> str:
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
    found_vowel = ''
    found_consonant = False
    
    for i in range(len(word) - 2, 0, -1):
        if word[i] in vowels:
            found_vowel = word[i]
            found_consonant = True
        elif word[i] in consonants and found_consonant:
            return found_vowel
    
    return ''
