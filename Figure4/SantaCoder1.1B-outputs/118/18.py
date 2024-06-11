def get_closest_vowel(word):
    
    vowels = ["a", "e", "i", "o", "u"]
    if word[0] in vowels and word[-1] in vowels:
        return word[0]
    elif word[0] in vowels:
        return word[0]
    elif word[-1] in vowels:
        return word[-1]
    else:
        return ""


