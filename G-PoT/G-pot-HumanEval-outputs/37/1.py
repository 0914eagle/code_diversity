
def get_closest_vowel(word: str) -> str:
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    found_consonant = False
    closest_vowel = ''
    
    for i in range(len(word) - 1, 0, -1):
        if word[i] in consonants:
            found_consonant = True
        elif word[i] in vowels and found_consonant:
            closest_vowel = word[i]
            break
    
    return closest_vowel
