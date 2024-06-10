
def is_consonant(char: str) -> bool:
    return char.isalpha() and char.lower() not in 'aeiou'

def get_closest_vowel(word: str) -> str:
    for i in range(len(word) - 2, 0, -1):
        if is_consonant(word[i]) and not is_consonant(word[i - 1]) and is_consonant(word[i - 2]):
            return word[i - 1] if word[i - 1].lower() in 'aeiou' else ''
    return ''

word = input().strip()
print(get_closest_vowel(word))
