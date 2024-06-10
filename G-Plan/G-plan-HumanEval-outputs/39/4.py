
def is_vowel(char: str) -> bool:
    return char.lower() in 'aeiou'

def get_closest_vowel(word: str) -> str:
    vowels = [i for i, c in enumerate(word) if is_vowel(c)]
    if len(vowels) < 2:
        return ''

    for i in range(len(word) - 2, 0, -1):
        if is_vowel(word[i]):
            for j in range(i - 1, 0, -1):
                if not is_vowel(word[j]):
                    return word[i].lower()
    return ''

word = input()
print(get_closest_vowel(word))
