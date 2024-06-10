
def is_vowel(char):
    return char.lower() in 'aeiou'

def is_consonant(char):
    return char.isalpha() and not is_vowel(char)

def get_closest_vowel(word: str) -> str:
    closest_vowel = ''
    for i in range(len(word) - 2, 0, -1):
        if is_consonant(word[i]) and is_vowel(word[i - 1]) and is_consonant(word[i - 2]):
            closest_vowel = word[i - 1]
            break
    return closest_vowel

word = input().strip()
print(get_closest_vowel(word))
