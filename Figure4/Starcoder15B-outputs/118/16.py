def get_closest_vowel(word):
    
    vowels = "aeiouAEIOU"
    vowel_index = -1
    for i in range(len(word)-1, -1, -1):
        if word[i] in vowels:
            vowel_index = i
            break
    if vowel_index == -1:
        return ""
    for i in range(vowel_index-1, -1, -1):
        if word[i] not in vowels:
            return word[i+1]
    return ""

