
def get_closest_vowel(word: str) -> str:
    vowels = set('aeiouAEIOU')
    consonants = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
    
    word = word.strip()
    if len(word) < 3:
        return ''
    
    for i in range(len(word) - 3, -1, -1):
        if word[i] in consonants and word[i+1] in vowels and word[i+2] in consonants:
            return word[i+1]
    
    return ''
