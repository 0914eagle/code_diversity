
def is_vowel(char: str) -> bool:
    return char.lower() in 'aeiou'

def get_closest_vowel(word: str) -> str:
    vowels = [i for i, c in enumerate(word) if is_vowel(c)]
    if len(vowels) < 2:
        return ''

    for i in range(len(word) - 2, 0, -1):
        if word[i] not in 'aeiou' and is_vowel(word[i - 1]) and word[i - 2] not in 'aeiou':
            return word[i - 1]

    return ''

word = input()
print(get_closest_vowel(word))
