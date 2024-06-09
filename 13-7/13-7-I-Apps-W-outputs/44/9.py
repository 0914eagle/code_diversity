
def beroffice_typo_fixer(word):
    vowels = set("aeiou")
    consonants = set("bcdfghjklmnpqrstvwxyz")
    typo_found = False
    for i in range(len(word) - 2):
        if word[i] in consonants and word[i + 1] in consonants and word[i + 2] in consonants:
            if len(set([word[i], word[i + 1], word[i + 2]])) > 1:
                typo_found = True
                break
    if typo_found:
        fixed_word = ""
        for i in range(len(word)):
            if i > 0 and word[i] in vowels and word[i - 1] in consonants:
                fixed_word += " "
            fixed_word += word[i]
        return fixed_word.strip()
    else:
        return word
