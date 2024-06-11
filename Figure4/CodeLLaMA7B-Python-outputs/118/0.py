def get_closest_vowel(word):
    
    # My and best solution
    vowels = "aeiouAEIOU"
    word = word.rstrip(vowels)
    word = word.lstrip(vowels)
    if len(word) < 2:
        return ""
    for i in range(len(word)-2, -1, -1):
        if word[i] in vowels and word[i+1] in vowels:
            return word[i]
    return ""


