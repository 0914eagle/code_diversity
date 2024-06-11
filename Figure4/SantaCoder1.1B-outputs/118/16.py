def get_closest_vowel(word):
    
    vowels = "aeiouAEIOU"
    if word[0] in vowels and word[-1] in vowels:
        return word[1:-1]
    else:
        return ""


