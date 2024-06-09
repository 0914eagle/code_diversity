
def get_closest_vowel(word: str) -> str:
    
    vowels = 'aeiouAEIOU'
    for i in range(len(word) - 1, -1, -1):
        if word[i] in vowels:
            if i < len(word) - 1 and word[i + 1].isalpha():
                return word[i]
    return ''

