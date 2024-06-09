
def check_typo(word):
    vowels = ["a", "e", "i", "o", "u"]
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    
    # Check if the word has any typos
    has_typo = False
    for i in range(len(word) - 2):
        if word[i] in consonants and word[i + 1] in consonants and word[i + 2] in consonants:
            if word[i] != word[i + 1] and word[i + 1] != word[i + 2]:
                has_typo = True
                break
    
    # If the word has a typo, insert spaces to fix it
    if has_typo:
        fixed_word = ""
        for i in range(len(word)):
            if i > 0 and word[i] in vowels and word[i - 1] in consonants:
                fixed_word += " "
            fixed_word += word[i]
        return fixed_word.strip()
    
    # If the word has no typos, return the original word
    else:
        return word

