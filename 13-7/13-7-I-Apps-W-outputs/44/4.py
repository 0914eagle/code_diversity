
def solve(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = [c for c in word if c not in vowels]
    if len(consonants) < 3:
        return word
    for i in range(len(consonants) - 2):
        if consonants[i] == consonants[i+1] == consonants[i+2]:
            continue
        if consonants[i] != consonants[i+1] and consonants[i+1] != consonants[i+2]:
            return word[:i+1] + ' ' + word[i+1:]
    return word

