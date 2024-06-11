def get_closest_vowel(word):
    
    vowels = ["a", "e", "i", "o", "u"]
    for vowel in vowels:
        if word.endswith(vowel):
            return vowel
    return ""


