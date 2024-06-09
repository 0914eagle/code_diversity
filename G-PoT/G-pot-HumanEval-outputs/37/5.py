
def get_closest_vowel(word: str) -> str:
    vowels = 'aeiouAEIOU'
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    
    word = word.strip(consonants)
    if len(word) < 3:
        return ''
    
    for i in range(len(word) - 2, 0, -1):
        if word[i] in vowels:
            return word[i]
    
    return ''
