def get_closest_vowel(word):
    
    vowels = "aeiouAEIOU"
    vowel_list = []
    for i in range(len(word)):
        if word[i] in vowels:
            vowel_list.append(i)
    if len(vowel_list) == 0:
        return ""
    if len(vowel_list) == 1:
        return word[vowel_list[0]]
    if len(vowel_list) == 2:
        return word[vowel_list[1]]
    if len(vowel_list) > 2:
        return word[vowel_list[-2]]

#