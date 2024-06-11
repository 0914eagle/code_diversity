def get_closest_vowel(word):
    
    vowels = "aeiouAEIOU"
    word = word[::-1]
    for i in range(len(word)):
        if word[i] in vowels:
            return word[i]
        elif word[i] not in vowels and i == len(word) - 1:
            return ""

# print(get_closest_vowel("yogurt"))
# print(get_closest_vowel("FULL"))
# print(get_closest_vowel("quick"))
# print(get_