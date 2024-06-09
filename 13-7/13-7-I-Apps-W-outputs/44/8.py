
def solve(word):
    vowels = ["a", "e", "i", "o", "u"]
    consonants = [char for char in word if char not in vowels]
    if len(consonants) < 3:
        return word
    else:
        spaces = []
        for i in range(len(consonants) - 2):
            if consonants[i] == consonants[i+1] == consonants[i+2]:
                continue
            elif consonants[i] == consonants[i+1] or consonants[i+1] == consonants[i+2]:
                spaces.append(i+1)
        for space in sorted(spaces, reverse=True):
            word = word[:space] + " " + word[space:]
        return word

