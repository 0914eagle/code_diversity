
def get_closest_vowel(word: str) -> str:
    
    vowels = ['a', 'e', 'i', 'o', 'u']
    word = word[::-1]
    for i in range(len(word)):
        if word[i] in vowels:
            if i > 0 and word[i-1].isalpha() and word[i+1].isalpha():
                return word[i]
    return ''

