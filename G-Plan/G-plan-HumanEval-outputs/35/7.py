
def is_vowel(char):
    return char.lower() in ['a', 'e', 'i', 'o', 'u']

def vowels_count(s: str) -> int:
    count = 0
    for i in range(len(s)):
        if is_vowel(s[i]):
            count += 1
        elif i == len(s) - 1 and s[i].lower() == 'y':
            count += 1
    return count

word = input()
print(vowels_count(word))
