
def solve(word):
    vowels = ["a", "e", "i", "o", "u"]
    consonants = [char for char in word if char not in vowels]
    if len(consonants) < 3:
        return word
    else:
        for i in range(len(consonants) - 2):
            if consonants[i] == consonants[i+1] == consonants[i+2]:
                return word
        return word[:i+1] + " " + word[i+1:]

