def get_closest_vowel(word):
    
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(word)):
        if word[i] in vowels:
            return word[i]
    return ""


