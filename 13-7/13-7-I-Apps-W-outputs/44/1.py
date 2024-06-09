
def solve(word):
    vowels = set("aeiou")
    consonants = set("bcdfghjklmnpqrstvwxyz")
    typos = 0
    for i in range(len(word) - 2):
        if word[i] in consonants and word[i + 1] in consonants and word[i + 2] in consonants:
            if len(set(word[i:i + 3])) > 1:
                typos += 1
                if typos > 2:
                    break
    if typos > 0:
        result = []
        for i in range(len(word)):
            if word[i] in vowels or i == len(word) - 1 or (word[i + 1] in vowels and word[i] in consonants):
                result.append(word[i])
                if i < len(word) - 1 and word[i] in consonants and word[i + 1] in consonants:
                    result.append(" ")
        return "".join(result)
    else:
        return word

