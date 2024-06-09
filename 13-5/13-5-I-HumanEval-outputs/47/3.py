
def get_closest_vowel(word: str) -> str:
    
    vowels = 'aeiouAEIOU'
    for i in range(len(word) - 1, 0, -1):
        if word[i] in vowels and word[i - 1] not in vowels and word[i + 1] not in vowels:
            return word[i]
    return ''

