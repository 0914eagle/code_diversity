def get_closest_vowel(word):
    
    if not word:
        return ""
    vowels = "aeiouAEIOU"
    for i in range(len(word)):
        if word[i] in vowels:
            return word[i]
    return ""


