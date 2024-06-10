
def is_vowel(char: str) -> bool:
    return char.lower() in ['a', 'e', 'i', 'o', 'u']

def get_closest_vowel(word: str) -> str:
    closest_vowel = ''
    for i in range(len(word) - 2, 0, -1):
        if not is_vowel(word[i]) and not is_vowel(word[i + 1]) and is_vowel(word[i - 1]):
            closest_vowel = word[i - 1]
            break
    return closest_vowel

word = input().strip()
print(get_closest_vowel(word))
