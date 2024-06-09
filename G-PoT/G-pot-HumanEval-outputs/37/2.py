
def get_closest_vowel(word: str) -> str:
    vowels = set('aeiouAEIOU')
    consonants = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
    closest_vowel = ''
    
    for i in range(len(word) - 3, 0, -1):
        if word[i] in vowels:
            for j in range(i + 1, len(word)):
                if word[j] in consonants:
                    closest_vowel = word[i]
                    break
            break
    
    return closest_vowel
