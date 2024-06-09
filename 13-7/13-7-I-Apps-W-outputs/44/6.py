
def solve(word):
    vowels = set("aeiou")
    consonants = set("abcdefghijklmnopqrstuvwxyz") - vowels
    typo_found = False
    for i in range(len(word) - 2):
        if word[i] in consonants and word[i + 1] in consonants and word[i + 2] in consonants:
            if len(set(word[i:i + 3])) > 1:
                typo_found = True
                break
    if typo_found:
        result = []
        for i in range(len(word)):
            if word[i] in consonants and word[i + 1] in consonants and word[i + 2] in consonants:
                if len(set(word[i:i + 3])) > 1:
                    result.append(word[i:i + 1])
                    result.append(" ")
                    i += 2
                else:
                    result.append(word[i:i + 3])
                    i += 2
            else:
                result.append(word[i])
        return "".join(result)
    else:
        return word

