
def check_vowel(c):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if c in vowels:
        return 'vowel'
    else:
        return 'consonant'

if __name__ == '__main__':
    c = input().strip()
    print(check_vowel(c))
