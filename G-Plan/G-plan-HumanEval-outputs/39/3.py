
def is_vowel(char):
    return char.lower() in 'aeiou'

def get_closest_vowel(word: str) -> str:
    for i in range(len(word) - 2, 0, -1):
        if not is_vowel(word[i]) and is_vowel(word[i - 1]) and not is_vowel(word[i - 2]):
            return word[i - 1]
    return ''

word = input().strip()
print(get_closest_vowel(word))
