
def check_vowel(c):
    vowels = {'a': 'vowel', 'e': 'vowel', 'i': 'vowel', 'o': 'vowel', 'u': 'vowel'}
    return vowels.get(c, 'consonant')

if __name__ == '__main__':
    c = input().strip()
    print(check_vowel(c))
