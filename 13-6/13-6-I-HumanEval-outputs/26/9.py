
def get_closest_vowel(word: str) -> str:
    
    vowels = 'aeiouAEIOU'
    if len(word) < 2:
        return ''
    for i in range(len(word)-2, -1, -1):
        if word[i] in vowels:
            return word[i]
    return ''

