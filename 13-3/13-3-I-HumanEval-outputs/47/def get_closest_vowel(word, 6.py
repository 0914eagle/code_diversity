
def get_closest_vowel(word: str) -> str:
    
    vowels = 'aeiouAEIOU'
    word = word[::-1]
    for i in range(len(word)):
        if word[i] in vowels:
            if i > 0 and word[i-1] in vowels:
                return word[i]
    return ''

