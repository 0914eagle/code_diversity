def get_closest_vowel(word):
    
    vowels = "aeiouAEIOU"
    word = word.strip()
    if len(word) < 3:
        return ""
    for i in range(len(word)-1, 0, -1):
        if word[i] in vowels and word[i-1] in vowels:
            return word[i]
    return ""


