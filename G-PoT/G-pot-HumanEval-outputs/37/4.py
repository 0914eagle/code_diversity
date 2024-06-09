
def get_closest_vowel(word: str) -> str:
    vowels = set('aeiouAEIOU')
    consonants = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
    
    word = word.strip(consonants)
    if len(word) < 3:
        return ''
    
    for i in range(len(word) - 3, -1, -1):
        if word[i] in vowels:
            return word[i]
    
    return ''
