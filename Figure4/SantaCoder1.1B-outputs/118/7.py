def get_closest_vowel(word):
    
    if word[0] in "aeiou":
        return word[0]
    elif word[0] in "AEIOU":
        return "A"
    elif word[0] in "O":
        return "O"
    elif word[0] in "U":
        return "U"
    elif word[0] in "a":
        return "a"
    elif word[0] in "e":
        return "e"
    elif word[0] in "i":
        return "i"
    elif word[0] in "o":
        return "o"
    elif word[0] in "u":
        return "u"
    else:
        return ""


